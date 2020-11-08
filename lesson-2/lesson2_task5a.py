# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Решение через бинарный поиск, так как рейтинги отсортированы

ratings = [7, 5, 3, 3, 2]

while True:
    user_rate = int(input('Введите рейтинг (целое неотрицательное число).\n'
                          'Чтобы закончить работу с программой введите отрицательное число: '))
    if user_rate < 0:
        break

    start = 0
    end = len(ratings)

    while start != end:
        i = (start + end) // 2
        if user_rate > ratings[i]:
            end = i
            continue
        elif user_rate < ratings[i]:
            start = i + 1
            continue
        else:
            ratings.insert(i, user_rate)
            break
    else:
        ratings.insert(start, user_rate)

    print('Рейтинг', ratings)
