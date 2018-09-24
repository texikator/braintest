# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Поехали!"

    def stop(self):
        return f'{self.name}  "Остановились"'

    def turn(self, direction):
        return f'{self.name}  "повернули" {direction}'


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Поехали!"

    def stop(self):
        return f'{self.name}  "Остановились"'

    def turn(self, direction):
        return f'{self.name}  "повернули" {direction}'


class WorkCar:

    def __init__(self, speed, color, name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Поехали!"

    def stop(self):
        return f'{self.name}  "Остановились"'

    def turn(self, direction):
        return f'{self.name}  "повернули" {direction}'


class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Поехали!"

    def stop(self):
        return f'{self.name}  "Остановились"'

    def turn(self, direction):
        return f'{self.name}  "повернули" {direction}'



#vaz = TownCar(90, "red", "***")
#print(vaz.turn("налево"))



# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car():
    def go(self):
        return "Поехали!"

    def stop(self):
        return f'{self.name}  "Остановились"'

    def turn(self, direction):
        return f'{self.name}  "повернули" {direction}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


vaz = TownCar(90, "red", "***",1)
print(vaz.turn("налево"))