# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
# атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    def __init__(self, art_title: str):
        self.title = art_title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Чертим карандашом')


class Handle(Stationery):
    def draw(self):
        print('Выделяем текст маркером')


some_stationery = Stationery('Some stationery')
some_pen = Pen('Parker')
some_pencil = Pencil('Faber Castell')
some_handle = Handle('Centropen')

print(some_stationery.title)
print(some_pen.title)
print(some_pencil.title)
print(some_handle.title)

some_stationery.draw()
some_pen.draw()
some_handle.draw()
some_pencil.draw()
