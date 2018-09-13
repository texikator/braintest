# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
'''
name = input("Введите имя: ")
age = input("Введите возраст: ")
city =  input("Введите город проживания: ")

def living(name,age,city):
    temp = ('{},  {} год, проживает в городе {}.'.format(name, age, city))
    return temp

print(living(name,age,city))
'''
#Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
array = []
for _ in range(3):
    i = input("ведите число: ")
    array.append(i)

def max_value(array):
    return max(array)1

print(max_value(array))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

array = ["test","ghfgh","dfgtgjurt","hjfoogo"]

def max_arg(*args):
    return max(args, key=len)

print(max_arg(*array))
