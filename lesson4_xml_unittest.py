"""
Тестируем функции заданий 6.6.1, 6.6.2, 6.6.3
"""

import xml.etree.ElementTree as ETree
import unittest
import os.path
from lesson4_xml_6_6_1 import node_list
from lesson4_xml_6_6_2 import node_parent
from lesson4_xml_6_6_3 import node_remove


class TestWork1(unittest.TestCase):
    """
    Testing 6.6.1
    """
    def setUp(self):
        """
        Открыть файл, спарсить его, получить корневой элемент.
        """
        self.filename = os.path.abspath('demo.xml')
        self.testfile = open(self.filename)
        # Спарсить файл.
        self.xml1 = ETree.parse(self.testfile)
        # Получить корневой узел
        self.root = self.xml1.getroot()

    def test_list(self):
        """
        Возвращает ли список
        """
        result = node_list(self.root, 'sex')
        self.assertIsInstance(result, list)

    def test_result(self):
        """
        Проверяем результат. Три тега.
        """
        # Подсчет количества тегов
        count = 0
        result = node_list(self.root, 'sex')
        # Посчитать сколько тегов содержится в списке.
        for arr in result:
            if 'sex' in str(arr):
                count += 1
        self.assertTrue(count, 3)

    def test_nothing(self):
        """
        Задать несуществующий тег
        """
        result = node_list(self.root, 'ptt')
        self.assertIsInstance(result, list)

    def test_not_root(self):
        """
        Задать не корневой узел
        """
        result = node_list(self.root[4], 'sex')
        self.assertTrue(result == [])

    def tearDown(self):
        """
        Закрыть файл
        """
        self.testfile.close()


class TestWork2(unittest.TestCase):
    """
    Testing 6.6.2
    """
    def setUp(self):
        """
        Открыть файл, спарсить его, получить корневой элемент.
        """
        self.filename = os.path.abspath('demo.xml')
        self.testfile = open(self.filename)
        # Спарсить файл.
        self.xml1 = ETree.parse(self.testfile)
        # Получить корневой узел
        self.root = self.xml1.getroot()

    def test_result(self):
        """
        Тест результата
        """
        result = node_parent(self.root, 'language')
        self.assertTrue(result == 'languages')

    def test_nothing(self):
        """
        Задать несуществующий тег
        """
        result = node_parent(self.root, 'ptt')
        self.assertIsNone(result)

    def test_list(self):
        """
        Возвращает ли строку
        """
        result = node_parent(self.root, 'sex')
        self.assertIsInstance(result, str)

    def tearDown(self):
        """
        Закрыть файл
        """
        self.testfile.close()


class TestWork3(unittest.TestCase):
    """
    Testing 6.6.3
    """
    def setUp(self):
        """
        Открыть файл, спарсить его, получить корневой элемент.
        """
        self.filename = os.path.abspath('demo2.xml')
        self.testfile = open(self.filename)
        # Спарсить файл.
        self.xml1 = ETree.parse(self.testfile)
        # Получить корневой узел
        self.root = self.xml1.getroot()

    def test_result(self):
        """
        Проверяем результат функции
        """
        # Подсчет количества тегов.
        count = 0
        # Выполнить функцию.
        node_remove(self.root, 'sex')
        # Записать измененную структуру в файл.
        self.xml1.write('demo2.xml')
        # Посчитать сколько удаленных тегов осталось.
        for item in self.root.iter():
            if item.tag == 'sex':
                count += 1
        # Должно остаться 0 тегов.
        self.assertTrue(count == 0)

    def tearDown(self):
        """
        Вернуть в файл удаленный тег и закрыть его.
        """
        itm_sex = ETree.SubElement(self.root, 'sex')
        itm_sex.text = 'true'
        self.xml1.write('demo2.xml')
        self.testfile.close()


if __name__ == '__main__':
    unittest.main()
