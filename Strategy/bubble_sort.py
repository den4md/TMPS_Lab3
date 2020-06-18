from Strategy.isort import ISort


class BubbleSort(ISort):
    def sort(self, arr: list) -> list:
        arr = list(arr)
        n = len(arr)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr
