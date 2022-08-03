"""
Printing only read values from the list
"""


def honest(array):
    """
    :param array: original list
    """
    if len(array) == 0:
        return
    if array[0] % 2 == 0:
        print(array[0])
    return honest(array[1:])
