"""
В работе опять первая четверть (правая верхняя)
Единицу в разряде тысяч не учитываем, ни в X, ни в Y, скорректировал условие с 25 до 23.
"""
import sys
import time
import numpy as np

from routins import sum_in_coordinates

size_x = 1000
size_y = 1000

sys.setrecursionlimit(900000000)

time_start = time.time()
res = np.full((1000, 1000), '?')


def check(x: int, y: int):
    # print(f"x: {x}, y: {y}")
    if size_x < x or size_y < y:
        return
    if res[x][y] in ['Y', 'N']:
        return
    if sum_in_coordinates(x, y) > 23:
        res[x][y] = 'N'
        return
    res[x][y] = 'Y'
    check(x + 1, y)     # Идем направо, песнь заводим
    check(x, y + 1)     # вверх


check(0, 0)
counter = (res == 'Y').sum()
time_end = time.time()
print(f'Правый верхний квадрат содержит {counter} клеток удовлетворяющих нашему условию')
print('Время выполнения:', time_end - time_start)

