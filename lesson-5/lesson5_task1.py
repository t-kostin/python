# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('lesson5_task1.txt', 'w', encoding='utf-8') as user_file:
    while True:
        user_input = input('Введите текст: ')
        if user_input == '':
            break
        user_file.write(user_input + '\n')
