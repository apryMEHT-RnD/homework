def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


#inner_function()    #при вызове ошибка
test_function()