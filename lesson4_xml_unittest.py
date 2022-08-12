"""
Тестируем функции заданий 6.6.1, 6.6.2, 6.6.3
"""

import xml.etree.ElementTree as ETree
import unittest
from lesson4_xml_6_6_1 import node_list
from lesson4_xml_6_6_2 import node_parent
from lesson4_xml_6_6_3_new_file import new_file
from lesson4_xml_6_6_3 import node_remove

# Спарсить файл.
xml1 = ETree.parse('demo.xml')
# Получить корневой узел
root = xml1.getroot()
# Создать новый файл для задания 6.6.3 - проверка удаления
new_file()


class TestWork1(unittest.TestCase):
    """
    Testing 6.6.1
    """
    def test_nothing(self):
        """
        Задать несуществующий тег
        """
        result = node_list(root, 'ptt')
        self.assertTrue(result == [])

    def test_not_root(self):
        """
        Задать не корневой узел
        """
        result = node_list(root[4], 'sex')
        self.assertTrue(result == [])

    def test_list(self):
        """
        Возвращает ли список
        """
        result = node_list(root, 'sex')
        self.assertIsInstance(result, list)


class TestWork2(unittest.TestCase):
    """
    Testing 6.6.2
    """
    def test_nothing(self):
        """
        Задать несуществующий тег
        """
        result = node_parent('ptt')
        self.assertIsNone(result)

    def test_list(self):
        """
        Возвращает ли строку
        """
        result = node_parent('sex')
        self.assertIsInstance(result, str)


class TestWork3(unittest.TestCase):
    """
    Testing 6.6.3
    """

    def test_result(self):
        """
        Проверяем результат
        """
        new_file()
        result = node_remove('sex')
        self.assertTrue(result, True)

    def test_root_only(self):
        """
        В файле только родительский тег
        """
        new_file()
        xml2 = ETree.parse('demo2.xml')
        root2 = xml2.getroot()
        root2.clear()
        xml2.write('demo2.xml')
        result = node_remove('sex')
        self.assertTrue(result, True)


if __name__ == '__main__':
    unittest.main()
