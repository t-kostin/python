# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

def get_hours(arg):
    if arg == '-':
        return 0
    else:
        par_pos = arg.index('(')
        return int(arg[:par_pos])


result = {}
with open('lesson5_task6.txt', 'r', encoding='utf-8') as source_file:
    while True:
        input_string = source_file.readline()
        if not input_string:
            break
        subject = input_string.split(':')
        hours = list(map(get_hours, subject[1].split()))
        result.update({subject[0]: sum(hours)})

print(result)