"""
B. Абстрактный кот
    При наследовании классов класс-наследник обычно имеет больший функционал, чем
родительский класс. А у котов все наоборот. Кошка по сравнению с котенком умеет ловить
мышей (котенок пока нет) и мяукает громче (CAPS LOCK'ом). Поэтому логично кошку
наследовать от котенка...
    Напишите классы:
    Класс АбстрактныйКот (AbstractCat), который инициализируется без аргументов. Умеет:
- eat - есть. За каждые 10 единиц еды вес увеличивается на 1 единицу, пока не станет 100,
дальше не растет. Если при одном приеме пищи количество еды не кратно 10, остаток
запасается, а потом суммируется с новой едой.
- возвращать строковое представление в виде <Имя класса> (вес).
    Класс Котенок (Kitten), наследуется от кота с аргументом вес. Умеет мяукать тоненько:
- meow - возвращает строку "meow..."
Еще умеет спать - sleep - возвращает строку Snore, повторенную столько раз, сколько число 5
помещается в весе.
    Класс Кошка (Cat), наследуется от котенка с аргументами вес и кличка. Умеет мяукать громко:
- meow - "MEOW..." и возвращать свое имя - get_name. Так же умеет ловить мышей:
- catch_mice - возвращает строку "Got it!"
"""


class AbstractCat:
    def __init__(self):
        self.weight = 0
        self.fat = 0

    def eat(self, food):
        if self.weight >= 100:
            self.weight = 100
        else:
            self.weight += (self.fat + food)//10
            self.fat = food%10

    def __str__(self):
        return "<{}> ({})".format(self.__class__.__name__, self.weight)


class Kitten(AbstractCat):
    def __init__(self, weight):
        self.weight = weight

    def meow(self):
        return "meow..."

    def sleep(self):
        return "Snore" * (self.weight//5)


class Cat(Kitten):
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def meow(self):
        return "MEOW..."

    def get_name(self):
        return self.name

    def catch_mice(self):
        return "Got it!"


abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)   #14
kit = Kitten(21)
print(kit.meow())
print(kit.sleep())
cat = Cat(83, "Molly")
print(cat.meow())
print(cat.get_name())
print(cat.catch_mice())
