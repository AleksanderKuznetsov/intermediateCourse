"""
Написать функцию, которая формирует список всех узлов
по заданному тегу в XML-документе.
"""
import xml.etree.ElementTree as ETree

# Спарсить файл.
xml1 = ETree.parse('demo.xml')
# Получить корневой узел
root = xml1.getroot()


def node_list(root_node, tag: str) -> list:
    """
    Сформировать список узлов по заданному тегу.
    Глубина вложенности узлов - не более двух.
    :param root_node: Корневой узел.
    :param tag: Тег.
    :return: Список узлов.
    """
    array = []
    # Проверить дочерние элементы корневого узла.
    if len(root_node.findall(tag)) > 0:
        array = root_node.findall(tag)
    # Проверить дочерние элементы первого уровня вложенности
    # и добавить в массив.
    for node in root_node:
        if len(node.findall(tag)) > 0:
            array.extend(node.findall(tag))
    return array
