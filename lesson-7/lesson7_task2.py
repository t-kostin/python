# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу
# этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
# уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, title, size):
        self.size = size
        super().__init__(title)

    @property
    def cloth_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothing):
    def __init__(self, title, height):
        self.height = height
        super().__init__(title)

    @property
    def cloth_consumption(self):
        return self.height * 2 + 0.3


def total_cloth_consumption(*args):
    return sum(map(lambda a: a.cloth_consumption, args))


first_suit = Suit('Armani', 1.82)
second_suit = Suit('Dolce Gabbana', 1.85)
coat = Coat('Gucci', 18)

print(f'Расход ткани на костюм {first_suit} (рост {first_suit.height} м) составит {first_suit.cloth_consumption}.')
print(f'Расход ткани на костюм {second_suit} (рост {second_suit.height} м) составит {second_suit.cloth_consumption}.')
print(f'Расход ткани на пальто {coat} (размер {coat.size}) составит {coat.cloth_consumption}.')
print(total_cloth_consumption(first_suit, second_suit, coat))
