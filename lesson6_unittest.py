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
        Сравнить результат работы функции с заведомо рассчитанным результатом
        """
        array = []
        for i in range(1, 1001):
            array.append(i)

        function_result = main(array, 10)

        self.assertTrue(function_result == 500500)





if __name__ == '__main__':
    unittest.main()

