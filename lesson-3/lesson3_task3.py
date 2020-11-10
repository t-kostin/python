# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a > b:
        if b < c:
            return a + c
    elif a < c:
        return b + c
    return a + b


x = my_func(1, 1, 2)
print(x)
