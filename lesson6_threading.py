"""
Напишите функцию, которая получает на вход большой список вещественных чисел
(например, 10 тысяч элементов, сгенерируйте их случайным образом),
и количество процессов (целое число), которое должно просуммировать этот массив по кусочкам.
Не используйте в решении join()
"""
import random
import time
from threading import Thread


def add_array(count: int) -> list:
    """
    Сформирование списка с заданным количеством вещественных чисел.
    :param count: длина списка
    :return: список
    """
    array = []
    for i in range(count):
        item = random.uniform(round(1, 4), round(5, 4))
        array.append(item)
    return array


def long_process(array: list, start: int,
                 step: int, results=[]) -> list:
    """
    Расчет суммы элементов списка. По заданию суммировать нужно по кусочкам.
    Поэтому при каждом запуске задается элемент, с которого начать и шаг цикла.
    :param array: исходный массив.
    :param start: стартовый элемент.
    :param step: шаг цикла.
    :param results: список.
    :return: список.
    """
    summa = 0
    for i in range(start, len(array), step):
        summa += array[i]
        # time.sleep(0.1)
    results.append(summa)
    return results


def main(array: list, n: int) -> int:
    """
    Главная функция.
    :param array: исходный список вещественных чисел.
    :param n: количество процессов.
    :return: сумма элементов
    """
    # Результирующий список из функции подсчета кусочками.
    result = []
    # Список процессов.
    threads = []
    # Переменная результата.
    count = 0

    # Наполнить список процессами.
    for i in range(n):
        thread = Thread(target=long_process, name=str(i), args=(array, i, n, result))
        threads.append(thread)

    # Запустить процессы
    for i in range(len(threads)):
        threads[i].start()
        time.sleep(0.5)

    # Убедиться, что процессы уже не работают
    while len(threads) > 0:
        if threads[0].is_alive():
            time.sleep(0.5)
        else:
            threads.pop()

    # Суммируем элементы результирующего массива.
    for res in result:
        count += res

    return count
