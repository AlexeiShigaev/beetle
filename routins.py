from functools import lru_cache


@lru_cache(1024)
def sum_digits(number: int) -> int:
    # print('number\t', number, end=", summ=")
    return sum(map(int, str(number)))


def sum_in_coordinates(c_x: int, c_y: int) -> int:
    return sum_digits(c_x) + sum_digits(c_y)

