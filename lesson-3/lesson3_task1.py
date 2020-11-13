# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_div(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return None


a = float(input('Делимое: '))
b = float(input('Делитель: '))
x = my_div(a, b)
if x is None:
    print('Делить на ноль нельзя')
else:
    print('Результат:', x)
