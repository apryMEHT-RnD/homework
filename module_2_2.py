first = int(input("введите первое число: "))
second = int(input("введите второе число: "))
third = int(input("введите третье число: "))
if first == second == second == third:
    print("3")
elif first == second or  second == third or third == first:
    print("2")
elif first != second and  second != third and third != first:               # либо коротко через оператор else
    print("0")
#else:
    #print("0")