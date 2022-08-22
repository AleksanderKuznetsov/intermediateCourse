"""
Функция с неограниченным количеством "одновременно" выполняющихся генераторов
long_process. В качестве входных данных этой функции используйте список из целых значений.
"""


def long_process(id, n):
    """
    Функция-генератор
    :param id: Id генератора.
    :param n: Количество итераций.
    :return: Сумма значений.
    """
    summ = 0
    for x in range(n):
        summ += x
        print(id, summ)
        if x < n-1:
            yield
        else:
            yield summ


def generator_process(array: list) -> dict:
    """
    Основная функция
    :param array: Исходный список
    :return: Словарь с результатами
    """
    max_count = 0  # Максимальное число в исходном массиве
    mass = []  # Массив генераторов
    result = {}  # Словарь результата

    # Найти максимальное число в исходном массиве.
    # Это будет количество итераций в обработке массива.
    for count in array:
        if count > max_count:
            max_count = count

    # Обработка исходного массива. Наполнить ключами словарь.
    # Добавить в массив генераторы.
    for i, arr in enumerate(array):
        result['id' + str(i)] = None
        mass.append(long_process('id' + str(i), array[i]))

    # Расчет результата генераторами.
    for count in range(max_count):
        for mas in range(len(mass)):
            if result['id' + str(mas)] is None:
                result['id' + str(mas)] = next(mass[mas])

    return result
