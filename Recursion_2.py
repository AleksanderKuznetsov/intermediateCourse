"""
Calculating the sum of the digits of a number.
"""


def sum_digits(number) -> int:
    """
    :param number: original number
    """
    if number == 0:
        return 0
    return sum_digits(number // 10) + number % 10
