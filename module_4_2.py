def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

inner_function # вызов функции inner_function вне функции test_function приводит к появлению ошибки