# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через dict

winter = 'зима'
spring = 'весна'
summer = 'лето'
autumn = 'осень'

seasons_dict = {
    1: winter,
    2: winter,
    3: spring,
    4: spring,
    5: spring,
    6: summer,
    7: summer,
    8: summer,
    9: autumn,
    10: autumn,
    11: autumn,
    12: winter
}

while True:
    try:
        month = int(input('Введите номер месяца от 1 до 12: '))
    except ValueError:
        print('Ошибка ввода! Ожидается целое число!')
        continue
    if 1 <= month <= 12:
        break
    print('Неверный номер месяца!')

print(f'Время года для месяца {month} - {seasons_dict[month]}.')
