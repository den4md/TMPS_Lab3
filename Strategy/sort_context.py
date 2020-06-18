from random import random

from Strategy.bubble_sort import BubbleSort
from Strategy.isort import ISort


# noinspection PyAttributeOutsideInit
class SortContext:

    def __init__(self, sort_strategy: ISort):
        self._array = []
        self.random()
        self.set_sort_strategy(sort_strategy)

    def set_sort_strategy(self, sort_strategy):
        if (sort_strategy is None) or (not isinstance(sort_strategy, ISort)):
            self._sort_strategy = BubbleSort()
        else:
            self._sort_strategy = sort_strategy

    def random(self, num=1000, max_value=5000, center_value=2500):
        self._array = [random()*max_value-center_value for _ in range(num)]

    def sort(self) -> list:
        return self._sort_strategy.sort(self._array)
