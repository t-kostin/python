# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

user_input = sys.argv[1:]
if len(user_input) == 1 and user_input[0] == '-h':
    print('Использование:\nlesson4_task1 <выработка в часах> <почасовая ставка> <премия>')
elif len(user_input) > 3:
    print('Слишком много параметров!')
else:
    try:
        user_input = list(map(float, user_input))
        print(user_input)
        is_positive = True
        for param in user_input:
            if param < 0:
                is_positive = False
                break
        if is_positive:
            print('Заработная плата:', user_input[0] * user_input[1] + user_input[2])
        else:
            print('Параметры должны быть неотрицательными числами.')
    except ValueError:
        print('Параметры должны быть числами.')
