import multiprocessing
import time
from functools import lru_cache

import numpy as np

# Размер квадрата для исследования. 1000х1000.
SIZE = 1000
NUMBER_OF_PROCESSES = 8


def calc_sum_process(tasks: multiprocessing.Queue, results: multiprocessing.Queue) -> None:
    @lru_cache(maxsize=None)
    def sum_digits(number: int) -> int:
        return sum(map(int, str(number)))

    print("start process {}".format(multiprocessing.current_process().name))
    for x, y in iter(tasks.get, 'STOP'):
        results.put((x, y, sum_digits(x) + sum_digits(y)))

    print("finish process {}".format(multiprocessing.current_process().name))


def main():
    # таблица результатов обхода клеток
    res = np.full((1000, 1000), '-')
    # Очередь на расчет суммы цифр
    tasks_queue = multiprocessing.Queue()
    # Очередь рассчитанных клеток
    results_queue = multiprocessing.Queue()

    processes = []
    for n in range(NUMBER_OF_PROCESSES):
        p = multiprocessing.Process(
            name=f"proc-{n}",
            target=calc_sum_process,
            args=(tasks_queue, results_queue)
        )
        processes.append(p)

    tasks_queue.put((0, 0))
    [p.start() for p in processes]
    new_task_index = 0

    exit_counter = 0
    while exit_counter < 100000:
        if results_queue.empty() and tasks_queue.empty():
            exit_counter += 1

        while results_queue.qsize():
            coord_x, coord_y, summ = results_queue.get()
            res[coord_x][coord_y] = 'N'
            if summ <= 23:
                res[coord_x][coord_y] = 'Y'
                # Озадачим проверить клетку сверху
                if coord_x + 1 < SIZE and res[coord_x + 1][coord_y] == '-':
                    tasks_queue.put((coord_x + 1, coord_y))
                    res[coord_x + 1][coord_y] = '?'
                # Озадачим проверить клетку справа
                if coord_y + 1 < SIZE and res[coord_x][coord_y + 1] == '-':
                    tasks_queue.put((coord_x, coord_y + 1))
                    res[coord_x][coord_y + 1] = '?'
            exit_counter = 0

    print('STOP.')
    for i in range(NUMBER_OF_PROCESSES):
        tasks_queue.put('STOP')

    return (res == 'Y').sum()


if __name__ == '__main__':
    time_start = time.time()
    counter = main()
    time_end = time.time()
    print(f'Правый верхний квадрат содержит {counter} клеток удовлетворяющих нашему условию')
    print('Время выполнения:', time_end - time_start)
