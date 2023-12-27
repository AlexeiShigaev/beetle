from functools import lru_cache


# @lru_cache(maxsize=None)
# def sum_digits(number: int) -> int:
#     summ = 0
#     while number:
#         summ += number % 10
#         number //= 10
#     return summ


# # @lru_cache(maxsize=None)
# def sum_digits(number: int) -> int:
#     return number % 10 + sum_digits(number // 10) if number else 0


@lru_cache(maxsize=None)
def sum_digits(number: int) -> int:
    # print('number\t', number, end=", summ=")
    return sum(map(int, str(number)))


def sum_in_coordinates(c_x: int, c_y: int) -> int:
    return sum_digits(c_x) + sum_digits(c_y)

