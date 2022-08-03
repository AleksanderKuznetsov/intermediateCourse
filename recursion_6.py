"""
Printing a list of elements with even indices
"""


def honest_index(array):
    """
    :param array: original list
    """
    if len(array) == 0:
        return
    print(array[0])
    array.pop(0)
    array.pop(0)
    return honest_index(array)
