# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы
# списка можно не запрашивать у пользователя, а указать явно, в программе.

test_list = [
    'Это строка',
    12,
    456.34,
    'Другая строка',
    [34, 'Третья строка'],
    {'key1': 'Четвертая', 'key2': 45},
    (45, 56),
    {45, 56},
    False,
    44+3j
]

for i in test_list:
    if type(i) is str:
        print('Обработка для строки', i)
    elif type(i) is int:
        print('Обработка для целого', i)
    elif type(i) is float:
        print('Обработка для вещественного', i)
    elif type(i) is list:
        print('Обработка для списка', i)
    elif type(i) is dict:
        print('Обработка для словаря', i)
    elif type(i) is tuple:
        print('Обработка для кортежа', i)
    elif type(i) is set:
        print('Обработка для множества', i)
    elif type(i) is bool:
        print('Обработка для булева', i)
    elif type(i) is complex:
        print('Обработка для комлексного', i)
    else:
        print('Это какой-то тип, которого я пока не знаю')
