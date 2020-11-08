# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните
# в переменные, выведите на экран.

spam_string = 'Spam'
surprise = 'испанская инквизиция'

some_number = 13
another_number = 56.345

print(spam_string)
print('Никто не ждал, а тут', surprise)
print('Пара чисел:', some_number, another_number)

some_number = input('Введите целое число: ')
another_number = input('Введите вещественное число: ')
spam_string = input('Теперь наберите какую нибудь строку: ')


print('Типы some_number, another_number, spam_string', type(some_number), type(another_number), type(spam_string))

some_number = int(some_number)
another_number = float(another_number)

print('Типы some_number, another_number, spam_string', type(some_number), type(another_number), type(spam_string))

print(some_number, another_number, spam_string)
