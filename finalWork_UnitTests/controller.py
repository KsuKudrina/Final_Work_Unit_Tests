from __future__ import annotations
class controller():

    def __init__(self, list1: list[int | float], list2: list[int | float]):
        self.list1 = list1
        self.list2 = list2

    def averages_lists(self) -> tuple[float, float]:
        average_1 = 0
        if self.list1:
            average_1 = sum(self.list1) / len(self.list1)
        average_2 = 0
        if self.list2:
            average_2 = sum(self.list2) / len(self.list2)
        return average_1, average_2

    def value_compare(self) -> None:
        average_1, average_2 = self.averages_lists()
        if average_1 > average_2:
            print('Первый список имеет большее среднее значение')
        if average_1 < average_2:
            print('Второй список имеет большее среднее значение')
        if average_1 == average_2:
            print('Средние значения равны')
