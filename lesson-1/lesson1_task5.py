# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Введите выручку компании: '))
expenses = int(input('Введите затраты компании: '))


if proceeds > expenses:
    profit = proceeds - expenses
    profitability = profit / proceeds
    print(f'Ваша компания работает с прибылью. Размер прибыли {profit}. Рентабельность {profitability:.2f}')
    staff_number = int(input('Введите количество сотрудников компании: '))
    profit_per_staff = profit / staff_number
    print(f'Прибыль на в расчете на одного сотрудника {profit_per_staff:.2f}')
else:
    loss = expenses - proceeds
    print(f'Ваша компания работает с убытком. Размер убытка {loss}.')
