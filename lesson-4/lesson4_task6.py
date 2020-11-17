# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle

start = 3
for i in count(start):
    if i > 10:
        break
    print(i)


count = 0
source = ['oak', 'birch', 'aspen', 'elm']
for i in cycle(source):
    print(i)
    count += 1
    if count >= 10:
        break
