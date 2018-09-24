# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, damage, armor):
        self._health = health
        self.name = name
        self._armor = armor
        self._damage = damage

    def strike_hits(self,target):
        strike_result = int(self.get_damage()/target.get_armor())
        target.set_health(strike_result)
        return target.get_health()

    def get_damage(self):
        return self._damage

    def get_armor(self):
        return self._armor

    def set_health(self, enemy_attack_force):
        self._health = self._health - enemy_attack_force

    def get_health(self):
        return self._health

    def get_name(self):
        return self.name

class Player(Person):

    def light_force(self):
        print("Да пребудет с тобой сила")

    def cure_force(self):
        print("Исцеляйся!")

class Enemy(Person):

    def dark_force(self):
        print("Переходите на темную сторону! У нас есть печеньки!")


class Fight:

    def __init__(self,person1,person2):
        self.person1 = person1
        self.person2 = person2

    def round(self):
        print(self.person1.name," vs ", self.person2.name)
        i = 1
        while True:
            if i % 2 == 0:
                #print(self.person1.get_name(), " kick ", self.person2.get_name())
                hit = self.person1.strike_hits(self.person2)
                #print(hit)
                if hit < 0:
                    winner = self.person1
                    break
            else:
                #print(self.person2.get_name(), " kick ", self.person1.get_name())
                hit = self.person2.strike_hits(self.person1)
                #print(hit)
                if hit < 0:
                    winner = self.person2
                    break
            i += 1
        return f'{winner.get_name()} Win'



djedi = Player(name = "Luk",health=100,damage=20,armor = 1.1)

sitkh = Enemy("sitkh1",100,30,1.3)

fight = Fight(djedi,sitkh)

print(fight.round())
