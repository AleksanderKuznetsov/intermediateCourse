"""
Написать функцию, которая удаляет все узлы
по заданному тегу в XML-документе
"""


def node_remove(root, tag: str) -> bool:
    """
    Возвращаем True скорее для тестов. Не по заданию.
    Глубина вложенности узлов - не более двух.
    :param root: Корневой элемент.
    :param tag: Тег.
    :return: True.
    """
    # Проверить дочерние элементы первого уровня вложенности
    # и добавить в массив.
    for node in root:
        # Проверить второй уровень вложенности.
        for sub_node in node[:]:
            if sub_node.tag == tag:
                node.remove(sub_node)
        # Проверить первый уровень вложенности.
        if node.tag == tag:
            root.remove(node)
    return True
