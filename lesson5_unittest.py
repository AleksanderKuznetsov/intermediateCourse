"""
Тестируем функции заданий 5.1, 5.2
"""

import unittest
from lesson5_iterators_1 import List1
from lesson5_iterators_2 import List2


class TestWork(unittest.TestCase):
    """
    Тестирование заданий 5.1 и 5.2
    """

    def test_result_1(self):
        """
        Задание 5.1. Тестирование общего результата.
        """
        array = []
        for n in List1(5):
            array.append(n)
        self.assertTrue(array == [5, 10, 20, 40, 80])

    def test_zero_1(self):
        """
        Задание 5.1. Тестирование нулей.
        """
        array = []
        for n in List1(0):
            array.append(n)
        self.assertTrue(array == [0, 0, 0, 0, 0])

    def test_big_number_1(self):
        """
        Задание 5.1. Тестирование большого числа.
        """
        array = []
        for n in List1(1589878545875121897156574984):
            array.append(n)
        self.assertTrue(array[-1] == 25438056734001950354505199744)

    def test_not_infinity_1(self):
        """
        Задание 5.1. Убедиться, что нет бесконечности.
        :return:
        """
        count = 0
        for n in List1(5):
            count += 1
        self.assertTrue(count == 5)

    def test_result_2(self):
        """
        Задание 5.2. Тестирование общего результата - не бесконечность.
        """
        array = []
        for n in List2(5, False):
            array.append(n)
        self.assertTrue(array == [1, 2, 4, 8, 16])

    def test_zero_2(self):
        """
        Задание 5.2. Тестирование нулей.
        """
        count = 0
        for n in List2(0, False):
            count += 1
        self.assertTrue(count == 0)

    def test_big_number_2(self):
        """
        Задание 5.1. Тестирование большого числа.
        """
        array = []
        for n in List2(100, False):
            array.append(n)
        self.assertTrue(array[-1] == 633825300114114700748351602688)


if __name__ == '__main__':
    unittest.main()

