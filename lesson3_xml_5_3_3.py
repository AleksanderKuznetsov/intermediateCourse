"""
Напишите функцию, которая возвращает количество узлов в документе,
включая дочерние, оснащённые заданным атрибутом.
"""

import xml.etree.ElementTree as ETree


def rec_tag(tag: str, items: list, array: list) -> list:
    """
    Рекурсивная функция.
    :param tag: Тег, который ищем.
    :param items: Сканируемый узел.
    :param array: Подсчет узлов.
    :return: Список array.
    """
    for i in range(len(items)):
        if tag in items[i].attrib.keys():
            array[0] += 1
        # Если в узле есть вложение.
        if len(items[i]) > 0:
            rec_tag(tag, items[i], array)

    return array[0]


def main(tag: str) -> list:
    """
    Основная функция. Отходим от глобальных переменных.
    :param tag: Искомый тег
    :return: Результат рекурсивной функции.
    """
    xml1 = ETree.parse('demo.xml')
    root = xml1.getroot()
    array = [0]
    return rec_tag(tag, root, array)
