immutable_var = tuple(["paper", "pen", "eraser", "clip", 100, 10, 50,])
#можем прописывать значения срахзу в скобах, без, через команду tuple.
#print(immutable_var)
#immutable_var = ("paper", "pen", "eraser", "clip", 100, 10, 50)
#print(immutable_var)
#immutable_var = "paper", "pen", "eraser", "clip", 100, 10, 50
print("Immutable tuple:", immutable_var)

#immutable_var [0] = 40    #кортеж является неизменяемым(используется в качестве хранилища),
#print(immutable_var)      #не поддерживает обращение по элементам, будет вылетать ошибка.

mutable_list = (["paper", "pen", "eraser", "clip", 100, 10, 50]) + (["pencil"])                                         #изменение элемента списка через сложение
print("Mutable list:", mutable_list)

mutable_list = ["paper", "pen", "eraser", "clip", 100, 10, 50]                                                          #изменение элемента списка через метод добавления вконце списка
mutable_list.append("pencil")
print("Mutable list:", mutable_list)

mutable_list = (["paper", "pen", "eraser", "clip"], 100, 10, 50)                                                        #замена одного из элементов списка
mutable_list [0] [1] = "pencil"
print("Mutable list:", mutable_list)