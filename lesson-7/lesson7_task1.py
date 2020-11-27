# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.

# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


def get_matrix_dim(arg_matrix):
    """
    Проверка, является ли аргумент целочисленной матрицей, т.е. удовлетворяет ли он след. условиям:
        1) Является списком ненулевой длины
        2) все его элементы являются списками ненулевой длины, содержат целые числа в
           качестве элементов и их длина одинакова.
    :param arg_matrix: список списков
    :return: Кортеж  (<количество строк>, <количество колонок>) если аргумент - целочисленная матрица
             None во всех остальных случаях
    """
    if type(arg_matrix) is list and len(arg_matrix):
        for line in arg_matrix:
            if not type(line) is list:
                return
            for col in line:
                if not type(col) is int:
                    return
        columns = len(arg_matrix[0])
        if columns == 0:
            return
        for line in arg_matrix:
            if len(line) != columns:
                return
        return len(arg_matrix), columns
    return


class MatrixArgError(Exception):
    pass


class Matrix:
    def __init__(self, arg_matrix):
        if get_matrix_dim(arg_matrix) is None:
            raise MatrixArgError('Argument is not a matrix of int values', arg_matrix)
        self.mtx = arg_matrix

    def __add__(self, other):
        first_dim = get_matrix_dim(self.mtx)
        if first_dim is None:
            raise MatrixArgError('Argument is not a matrix of int values', self.mtx)
        second_dim = get_matrix_dim(other.mtx)
        if second_dim is None:
            raise MatrixArgError('Argument is not a matrix of int values', other.mtx)
        if first_dim != second_dim:
            raise MatrixArgError('Matrices dimensions is not equal', first_dim, second_dim)
        result_mtx = []
        for line_1, line_2 in zip(self.mtx, other.mtx):
            result_line = []
            for elem_1, elem_2 in zip(line_1, line_2):
                result_line.append(elem_1 + elem_2)
            result_mtx.append(result_line)
        return Matrix(result_mtx)

    def __str__(self):
        result = ''
        for line in self.mtx:
            for column in line:
                result += '{:5} '.format(column)
            result += '\n'
        return result


matrix_1_5x6 = [[i + j for i in range(5)] for j in range(6)]
matrix_2_5x6 = [[(i + 1) * (j + 1) for i in range(5)] for j in range(6)]
matrix_4x7 = [[(i + j) * 2 for i in range(4)] for j in range(7)]

m1 = Matrix(matrix_1_5x6)
m2 = Matrix(matrix_2_5x6)
m_diff = Matrix(matrix_4x7)
result = m1 + m2

print(m1)
print(m2)
print(result)

# Пробуем сложить матрицы разных размеров
try:
    result = m1 + m_diff
except MatrixArgError:
    print('Сложить матрицы разных размеров нельзя')

# Пробуем получить экземпляр класса, используя неправильный аргумент
try:
    m3 = Matrix([[1, 3, 5], [1, 4, 'Yes'], [5, 6, 7]])
except MatrixArgError:
    print('Неправильный аргумент при создании экземпляра класса Matrix')

try:
    m3 = Matrix([[1, 3, 5], [1, 4], [5, 6]])
except MatrixArgError:
    print('Неправильный аргумент при создании экземпляра класса Matrix')
