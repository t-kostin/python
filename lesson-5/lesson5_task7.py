# Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).

import json

gross_profit = 0
company_count = 0
companies = {}
with open('lesson5_task7-1.txt', 'r', encoding='utf-8') as source_file:
    for source_line in source_file:
        source_list = source_line.split()
        profit = int(source_list[-2]) - int(source_list[-1])
        if profit >= 0:
            gross_profit += profit
            company_count += 1
        companies.update({' '.join(source_list[:-3]): profit})

result = [companies, {'average_profit': gross_profit / company_count}]

with open('lesson5_task7-2.json', 'w', encoding='utf-8') as target_file:
    json.dump(result, target_file)
