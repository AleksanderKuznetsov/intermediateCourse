"""
Напишите функцию, которая формирует список всех значений
(по всем узлам) для конкретного тега, если задано его название
"""

import xml.etree.ElementTree as ETree


def rec_tag(tag, items, array):
    """
    Рекурсивная функция.
    :param tag: Тег, который ищем.
    :param items: Сканируемый узел.
    :param array: Список, в который добавляем найденные значения тега.
    :return: Список array.
    """
    for i in range(len(items)):
        if items[i].tag == tag:
            array.append(items[i].text)
        # Если в узле есть вложение.
        if len(items[i]) > 0:
            rec_tag(tag, items[i], array)

    return array


def main(tag):
    """
    Основная функция. Отходим от глобальных переменных.
    :param tag: Искомый тег
    :return: Результат рекурсивной функции.
    """
    xml1 = ETree.parse('demo.xml')
    root = xml1.getroot()
    array = []
    return rec_tag(tag, root, array)


print(main('test'))
