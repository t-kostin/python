# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


current_line = 0
file_info = {}
with open('lesson5_task2.txt', 'r', encoding='utf-8') as user_file:
    for current_string in user_file:
        current_line += 1
        words_in_line = len(current_string.split())
        file_info.update({current_line: words_in_line})
print(file_info)
print('Количество строк:', current_line)