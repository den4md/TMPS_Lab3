from Strategy.isort import ISort


class QuickSort(ISort):
    def sort(self, arr: list) -> list:
        low = 0
        high = len(arr) - 1

        arr = list(arr)
        self._sort(arr, low, high)
        return arr

    def _sort(self, arr: list, low: int, high: int) -> None:
        if low < high:
            pi = self.partition(arr, low, high)

            self._sort(arr, low, pi - 1)
            self._sort(arr, pi + 1, high)

    @staticmethod
    def partition(arr: list, low: int, high: int) -> int:
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
