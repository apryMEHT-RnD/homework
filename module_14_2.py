import sqlite3

connection = sqlite3.connect("not_telegram(14_2).db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)     
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"newuser{i+1}", f"example{i+1}@mail.ru", f"{(i+1)*10}", "1000"))

cursor.execute("UPDATE Users SET balance = ? WHERE id%2 <> ?", (500, 0))

cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(f'Средний баланс: {all_balances/total_users}')

connection.commit()
connection.close()