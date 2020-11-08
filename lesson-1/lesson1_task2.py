# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('Введите время в секундах: '))

hours = time_in_seconds // 3600
minutes = time_in_seconds % 3600 // 60
seconds = time_in_seconds % 3600 % 60

# разные варианты форматирования строк для достижения одинакового результата
print('Время ЧЧ:ММ:СС - %02d:%02d:%02d.' % (hours, minutes, seconds))
print('Время ЧЧ:ММ:СС - {:02}:{:02}:{:02}.'.format(hours, minutes, seconds))
print(f'Время ЧЧ:ММ:СС - {hours:02}:{minutes:02}:{seconds:02}.')
