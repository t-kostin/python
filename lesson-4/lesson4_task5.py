# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

import functools

result = [number for number in range(100, 1001, 2)]
result_sum = functools.reduce(lambda arg1, arg2: arg1 * arg2, result)

print(result)
print(result_sum)
