name = input("Введите ваше имя: ")
print("Привет " + name)

var = int(input("Введите число: "))
#var = var + 2
print("число +2 = " + str(var+2))

age = int(input("Введите ваш возраст"))
if age >= 18:
    print("Доступ разрешен")
    print("Добро пожаловать в наш бар")
    num = int(input("введите количество стаканов:"))
    if num == 1:
        count = " один "
    elif num == 2:
        count = " два "
    elif num == 3:
        count = " три "
    elif num > 3:
        print("Вы точно сможете выползти из бара ?")
    if num:
        print("Вот ваши " + str(num) + " стакана(ны/нов)")
else:
        print("Доступ запрещен")
