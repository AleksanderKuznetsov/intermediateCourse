"""
List2 получает количество N итерируемых элементов и флажок конечности/бесконечности.
В случае конечности List2 выдаёт N элементов и завершает работу,
а в случае бесконечности начинает повторно выдавать свою последовательность
с самого начала
"""


class List2:
    """
    Метод __init__ - начальные значения
    Метод __iter__ - начальная инициализация итератора
    Метод __next__ - следующее значение
    """
    def __init__(self, stop: int, flag: bool):
        """

        :param stop: Сколько итераций провести.
        :param flag: True - бесконечность. False - НЕбесконечность
        """
        self.stop = stop
        self.flag = flag

    def __iter__(self):
        self.start = 1
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1

        # Подсчет значений. Работает и для True и для False.
        if self.count <= self.stop:
            return current

        # Если бесконечность, возвращаемся к __iter__
        if self.flag:
            self.__iter__()
            return self.__next__()

        # Генерируем исключение, если выбрана не бесконечность
        # и параметр N меньше или равен заданной величине.
        raise StopIteration
