def send_email(message, recipient, *, sender):
    if not ('@' in recipient and '@' in sender and sender.endswith(('.com', '.ru', '.net')) and recipient.endswith(
            ('.com', '.ru', '.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо  отправлено с адреса {sender} на адрес {recipient}")


send_email('message', 'vasyok1337@gmail.com', sender="university.help@gmail.com")
send_email("message", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email('message', "urban.student@mail.ru", sender="urban.teacher@mail.uk")
send_email("message", "university.help@gmail.com", sender="university.help@gmail.com")
