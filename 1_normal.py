print("ВВедите число от 0 до 10")
while True:
    i = int(input("Введите число: "))
    if i > 0 and i < 10:
        print("Результат: " + str(i**2) )
        break
    else:
        print("Вы ввели неправильное число")


a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
a = a + b
b = a - b
a = a - b
print("Кручу, верчу...... ")
print("A = " + str(a) + ", B = " + str(b))