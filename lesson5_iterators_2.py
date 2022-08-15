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

        # Если в параметре бесконечность и счетчик self.count вышел за
        # пределы параметра N, обнулить первоначальные счетчики.
        if not self.flag and self.count > self.stop:
            self.count = 0
            self.start = 1

        # Подсчет значений
        if self.count <= self.stop:
            return current

        # Генерируем исключение, если выбрана не бесконечность
        # и параметр N меньше или равен заданной величине.
        raise StopIteration


for n in List2(10, False):
    print(n)
