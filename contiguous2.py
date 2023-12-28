"""
В работе опять первая четверть (правая верхняя)
Единицу в разряде тысяч не учитываем, ни в X, ни в Y, скорректировал условие с 25 до 23.
"""
import time
import numpy as np

from routins import sum_in_coordinates

size_x = 1000
size_y = 1000
cache = np.load('cache1000.npy')
res = np.full((1000, 1000), '?')


def sum_in_coordinates1(c_x: int, c_y: int) -> int:
    return cache[c_x] + cache[c_y]


def check(x: int, y: int):
    # print(f"x: {x}, y: {y}")
    if size_x < x or size_y < y:
        return
    if res[x][y] in ['Y', 'N']:
        return
    if sum_in_coordinates1(x, y) > 23:
        res[x][y] = 'N'
        return
    res[x][y] = 'Y'
    check(x + 1, y)     # Идем направо, песнь заводим
    check(x, y + 1)     # вверх


if __name__ == '__main__':

    time_start = time.time()

    check(0, 0)
    counter = (res == 'Y').sum()
    # for i in range(1000):
    #     cache[i] = sum(map(int, str(i)))
    # np.save('cache1000', cache)

    time_end = time.time()

    print(f'Правый верхний квадрат содержит {counter} клеток удовлетворяющих нашему условию')
    print('Время выполнения:', time_end - time_start)
