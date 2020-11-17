# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

result = [number for number in range(20, 241) if not (number % 20 and number % 21)]

print(result)
