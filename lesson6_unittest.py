"""
Тестируем задание 6
"""

import unittest
from lesson6_threading import *


class TestWork(unittest.TestCase):
    """
    Тестирование задания 6
    """

    def test_result(self):
        """
        Сравнить результат работы функции с перебором циклом
        """
        array = add_array(100000)
        function_result = main(array, 10)

        loop_result = 0
        for arr in array:
            loop_result += arr

        self.assertTrue(round(function_result, 4) == round(loop_result, 4))


if __name__ == '__main__':
    unittest.main()

