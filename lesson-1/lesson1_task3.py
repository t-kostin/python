# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = input('Введите целое положительное число: ')

number_double = int(number * 2)
number_triple = int(number * 3)
number = int(number)
number_sum = number + number_double + number_triple

print(f'Сумма {number}, {number_double} и {number_triple} равна {number_sum}.')
