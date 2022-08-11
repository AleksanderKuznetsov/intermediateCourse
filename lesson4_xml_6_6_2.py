"""
Написать функцию, которая находит родителя заданного узла,
и возвращает его (тип Element).
"""
import xml.etree.ElementTree as ETree

# Спарсить файл.
xml1 = ETree.parse('demo.xml')
# Получить корневой узел
root = xml1.getroot()


def node_parent(tag: str) -> str:
    """
    Вернуть родительский элемент.
    Проверяем наличие искомого тега в дочерних элементах
    и возвращаем родителя, если нашли.
    :param tag: Тег искомого узла.
    :return: Родительский элемент..
    """
    # Проверить дочерние элементы корневого узла.
    if len(root.findall(tag)) > 0:
        return root.tag
    # Проверить дочерние элементы первого уровня вложенности.
    for node in root:
        if len(node.findall(tag)) > 0:
            return node.tag
