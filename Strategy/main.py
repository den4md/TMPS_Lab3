from time import time

from Strategy.bubble_sort import BubbleSort
from Strategy.quick_sort import QuickSort
from Strategy.sort_context import SortContext


def time_sort(sort_context: SortContext):
    start_time = time()
    sort_context.sort()
    end_time = time()

    print(f'This sort took {end_time-start_time} s')


if __name__ == '__main__':
    context = SortContext(BubbleSort())

    print("Sorting of 1000 elements w/ Bubblesort")
    time_sort(context)

    print("Sorting of 1000 elements w/ Quicksort")
    context.set_sort_strategy(QuickSort())
    time_sort(context)
