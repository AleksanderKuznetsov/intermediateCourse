"""
calculation of the length of a list for which only
one operation of removing the first element is allowed pop(0)
"""


def len_list(array):
    """
    :param array: start array
    :return: count
    """
    if len(array) == 0:
        return 0
    array.pop(0)
    return len_list(array) + 1
