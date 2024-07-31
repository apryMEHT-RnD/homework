grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rating_log = {}
list_of_students = sorted(students)
average_score = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
                 sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
rating_log = {list_of_students [0] : average_score [0], list_of_students [1] : average_score [1], list_of_students [2] : average_score [2],
              list_of_students [3] : average_score [3], list_of_students [4] : average_score [4]}
print(rating_log)















