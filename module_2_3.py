my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    list_1 = my_list[index]
    index += 1
    if list_1 == 0:
        continue
    elif list_1 < 0:
        break
    else:
        print(list_1)
