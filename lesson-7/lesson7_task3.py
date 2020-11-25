# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления
# должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.

class Cell:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self.size <= other.size:
            print('Вычитание клеток выполнить невозможно')
        else:
            return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, arg_row):
        rows = self.size // arg_row
        last_row_len = self.size % arg_row
        return rows * (arg_row * '*' + '\n') + last_row_len * '*' + ('\n' if last_row_len else '')


first_cell = Cell(154)
second_cell = Cell(25)

added = first_cell + second_cell
subtracted = first_cell - second_cell
multiplied = first_cell * second_cell
divided = first_cell / second_cell

print('Сложение', added.size)
print('Умножение', multiplied.size)
print('Вычитание', subtracted.size)
print('Деление', divided.size)

subtraction_impossible = second_cell - first_cell
print('При невозможносьти вычитания возвращается', subtraction_impossible)

print(second_cell.make_order(8))
