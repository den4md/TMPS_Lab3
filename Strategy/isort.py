from abc import ABC, abstractmethod


class ISort(ABC):

    @abstractmethod
    def sort(self, arr: list) -> list:
        pass
