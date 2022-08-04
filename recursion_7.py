"""
Нахождение второго максимального числа в списке
(с учётом, что максимальных может быть несколько, если они равны)
"""


def rec(array: list, max1: int, max2: int) -> int:
    """
    Рекурсивная функция. Перебор элементов списка.
    :param array: Список на вход.
    :param max1: Первое максимальное известное число.
    :param max2: Второе максимальное известное число.
    :return: max2
    """
    # Выход из рекурсии. Возвращаем max2.
    if len(array) == 0:
        return max2
    # Первый элемент текущего списка больше max1.
    if array[0] >= max1:
        max2 = max1
        max1 = array[0]
    # Первый элемент текущего списка - среднее значение
    # (больше max2, но меньше max1).
    elif array[0] > max2:
        max2 = array[0]
    # Рекурсией перебираем список, откидывая 1й элемент на каждой итерации.
    return rec(array[1:], max1, max2)


def max_snd(array):
    """
    Основная функция
    :param array: Исходный список.
    :return: max2 (в результате рекурсии).
    """
    # Если список менее двух элементов
    if len(array) < 2:
        return "Список менее двух элементов"
    # Проверяем первые два элемента списка
    # и выстраиваем переменные по их по убыванию.
    if array[0] > array[1]:
        max1 = array[0]
        max2 = array[1]
    else:
        max1 = array[1]
        max2 = array[0]
    # Возвращаем результат рекурсивной функции.
    # Подаем на вход список с третьего элемента, т.к. первые два уже обработали.
    return rec(array[2:], max1, max2)
