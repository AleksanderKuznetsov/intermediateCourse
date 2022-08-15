"""
Создать из класса List2 итератор с конструктором,
чтобы он работал с любого заданного значения.
"""


class List2:
    """
    Метод __init__ - начальное значение
    Метод __iter__ - начальная инициализация итератора
    Метод __next__ - следующее значение
    """
    def __init__(self, start: int):
        self.first = start

    def __iter__(self):
        self.start = self.first
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < 10:
            return current
        raise StopIteration


for n in List2(10):
    print(n)
