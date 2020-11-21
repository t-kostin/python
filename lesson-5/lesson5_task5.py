# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

output_list = [str(randint(1, 100)) for number in range(15)]

with open('lesson5_task5.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(' '.join(output_list)+'\n')

with open('lesson5_task5.txt', 'r', encoding='utf-8') as source_file:
    input_list = map(int, source_file.readline().split())

total_sum = sum(input_list)
print(f'сумма всех чисел в файле равна {total_sum}')
