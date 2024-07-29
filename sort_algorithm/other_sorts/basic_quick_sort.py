"""
Классическая быстрая сортировка.
"""


import random
from typing import List


def lomuto_partion(array: List[int], left: int, right: int) -> int:
    i = left - 1
    pivot_idx = random.randint(left, right)
    array[right], array[pivot_idx] = array[pivot_idx], array[right]
    pivot = array[right]
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]
    return i + 1


def quicksort_inplace(array: List[int], left: int, right: int) -> None:
    """Быстрая сортировка.

    Args:
        array (List[int]): массив для сортировки
    Returns:
        List[int]: отсортированный массив.
    """
    if left < right:
        center_idx = lomuto_partion(array, left, right)
        quicksort_inplace(array, left, center_idx-1)
        quicksort_inplace(array, center_idx+1, right)


def quicksort(array: List[int]) -> None:
    quicksort_inplace(array, 0, len(array) - 1)
