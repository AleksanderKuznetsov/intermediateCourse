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
    :param array: исходный список
    :return: словарь результата расчетов
    """
    result = {}  # словарь результата расчетов.
    dict = {}  # словарь генератора.
    processing = {}  # словарь обработанных элементов.

    # Создать словарь результата расчетов, запустить генератор по ключам.
    i = 0
    while len(result) != len(array):
        result[i] = None
        dict[i] = long_process(i, array[i])
        i += 1

    i = 0
    while len(processing) != len(array):
        # Если расчет не окончен - продолжить работу генератора
        if result[i] is None:
            result[i] = next(dict[i])

        # Если расчет окончен - внести этот элемент в словарь
        # обработанных элементов.
        elif result[i] is not None:
            processing[i] = True

        # Прибавить счетчик.
        i += 1
        # Обнулить счетчик.
        if i == len(array):
            i = 0

    return result
