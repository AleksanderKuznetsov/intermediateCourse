"""
Поиск всех файлов в заданном каталоге, включая файлы,
расположенные в подкаталогах произвольной вложенности
"""

import os.path


def rec(path: str, mass_file: list) -> list:
    """
    Рекурсивная функция.
    :param path: Путь к элементу.
    :param mass_file: Массив с файлами.
    :return: Массив с файлами, дополненный в результате функции.
    """
    # Циклом пройдем по элементам каталога
    for i in os.listdir(path):
        # Если элемент - каталог, рекурсией провалимся на уровень ниже.
        if os.path.isdir(os.path.join(path, i)):
            rec(os.path.join(path, i), mass_file)
        # Если элемент - файл, отложим название в список.
        elif os.path.isfile(os.path.join(path, i)):
            mass_file.append(i)
    return mass_file


def scan_top_level(path: str) -> list:
    """
    Основная функция.
    :param path: Путь к каталогу
    :return: Список файлов
    """
    # Задаем пустой каталог, чтобы подать его в рекурсивную функцию.
    mass_file = []

    return rec(path, mass_file)
