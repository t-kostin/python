# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Решение через прямой линейный поиск

ratings = [7, 5, 3, 3, 2]

while True:
    user_rate = int(input('Введите рейтинг (целое неотрицательное число).\n'
                          'Чтобы закончить работу с программой введите отрицательное число: '))
    if user_rate < 0:
        break

    no_insert = True
    for i, element in enumerate(ratings):
        if user_rate > element:
            ratings.insert(i, user_rate)
            no_insert = False
            break
    if no_insert:
        ratings.insert(len(ratings), user_rate)

    print('Рейтинг', ratings)
