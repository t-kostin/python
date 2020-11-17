# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

staff_number = 0
gross_salary = 0
with open('lesson5_task3.txt', 'r', encoding='utf-8') as user_file:
    while True:
        file_line = user_file.readline()
        if not file_line:
            break
        staff_number += 1
        staff_record = file_line.split()
        staff_record[1] = int(staff_record[1])
        gross_salary += staff_record[1]
        if staff_record[1] < 20000:
            print(f'{staff_record[0]} - зарплата {staff_record[1]}.')
print(f'Средняя зарплата {gross_salary / staff_number:.2f}.')
