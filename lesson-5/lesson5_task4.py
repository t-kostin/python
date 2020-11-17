# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

translate = dict(One='Один', Two='Два', Three='Три', Four='Четыре')

source_file = open('lesson5_task4-1.txt', 'r', encoding='utf-8')
target_file = open('lesson5_task4-2.txt', 'w', encoding='utf-8')

while True:
    current_line = source_file.readline()
    if not current_line:
        break
    current_record = current_line.split()
    current_record[0] = translate[current_record[0]]
    result_line = ' '.join(current_record) + '\n'
    target_file.write(result_line)

source_file.close()
target_file.close()
