"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
import re

class Card:


    def __init__(self,holder="Игрок"):
        self.left = 15
        self.holder = holder
        self.filed = []
        self._card_text = ""
        self.card_data = []
        self.fill_data()
        self.get_draw()
        #self.fill_card()


    def fill_data(self):
        for i in range(1,4):
            #self.card_data.append([])
            row = []
            position = 0

            for j in range(1,6):
                while True:
                    rand = random.randrange(1,90)
                    if rand not in self.filed:
                        self.filed.append(rand)
                        row.append(rand)
                        break
            row = sorted(row)
            self.card_data.append(row)


    def get_draw(self):
        string = ""
        top = ""
        top = self.holder.rjust(12-len(self.holder)//2,"-").ljust(26,"-")
        delim = ""

        for _ in range(26):
            delim += "-"
        string += top
        string += "\n"
        for i in range(0,3):
            position = 1
            for j in range(0,5):
                if 9 - position - j > 0:
                       while (random.randrange(2) == 0) and (9 - position - j > 0):
                           string += "   "
                           position += 1
                string += str(self.card_data[i][j]).rjust(2) + " "
                position += 1
            string += "\n"
        string += delim
        self._card_text = string

    def draw_r(self):
        return self.card_data

    def refil_draw(self,stroked):
        tmp = ""
        str_replace = ""
        reg = "("+str(stroked).rjust(2)+")\\b"
        tmp = re.sub(reg, "--", self._card_text)
        self._card_text = tmp
        return self._card_text  + "\n "\


    def get_card(self):
        return  self._card_text

    def check_number(self,number):
        if number in self.filed:
            self.refil_draw(number)
            self.left -= 1
            return self.left


class Human(Card):

    def decission(self):
        decission = ""
        while decission not in ("y","n"):
            decission = input("Зачеркнуть цифру (y,n)?")
        return decission


class Computer(Card):

    def decission(self):
        decission = "y" #random.randrange("Y","N")
        return decission


class Game:

    def __init__(self,gamers):

        self.barrels = [_ for _ in range(1, 91)]
        random.shuffle(self.barrels)
        self.gamers = gamers
        self.left = 15
        self.iteration = 0
        self.checked = ""


    def rounds(self):
        i = 0
        while i<90:
            print("Выпал номер", self.barrels[i])
            print("Уже выпали: ", self.checked)

            for gamer in self.gamers:
                print(gamer.get_card())
                print("Осталось: ", gamer.left)
                if self.barrels[i] in gamer.filed:
                    if gamer.decission() == "y":
                        result = gamer.check_number(self.barrels[i])
                        if result == 0:
                            print("Gamer ", gamer.holder, " win!")
                            exit()
            self.checked += str(self.barrels[i])
            self.checked += " "
            i += 1


comp = Computer("Компьютер")
user = Human("Человек")

gamers =[]
gamers.append(user)
gamers.append(comp)

new_game = Game(gamers)
new_game.rounds()


