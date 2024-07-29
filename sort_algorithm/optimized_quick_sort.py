"""
Оптимизированная быстрая сортировка (Quick sort).

Автор: Кирюшин Виталий
"""


import random
import time
from typing import List


MAX_ARRAY_SIZE = 16  # Размер массива который сортируется вставками


def insertion_sort(array: List[int], left: int, right: int) -> List[int]:
    """
    Сортировка вставками.

    Args:
        array (List[int]): исходный массив
        left (int): левая граница сортируемой части массива
        right (int): правая граница сортируемой части массива

    Returns:
        List[int]: отсортированный массив
    """
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        while j >= left and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def median_pivot(arr: List[int], left: int, right: int) -> int:
    """Функция выбора опорного элемента, по правилу медианы из трёх.

    Args:
        arr (List[int]): Сортируемый массив
        left (int): Левая граница
        right (int): Правая граница

    Returns:
        int: Опорная точка
    """
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    return arr[mid]


def hoare_partition(array: List[int], left: int, right: int) -> int:
    """Функция разбиения Хоара.

    Args:
        array (List[int]): Сортируемый массив
        left (int): Левая граница
        right (int): Правая граница
    """
    pivot_idx = median_pivot(array, left, right)
    pivot = pivot_idx
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def optimized_quicksort(array: List[int]) -> None:
    """Оптимизированная рекурсивная быстрая сортировка.

    Args:
        array (List[int]): Сортируемый массив
        left (int): Левая граница
        right (int): Правая граница
    """
    left, right = 0, len(array) - 1
    while left < right:
        if right - left < MAX_ARRAY_SIZE:
            insertion_sort(array, left, right)
            break
        else:
            mid = hoare_partition(array, left, right)
            if mid - left < right - mid:
                optimized_quicksort(array[left:mid])
                left = mid + 1
            else:
                optimized_quicksort(array[mid+1:right])
                right = mid


if __name__ == "__main__":
    array_0 = [random.randint(0, 1000000) for _ in range(1000000)]
    start_time = time.thread_time()
    optimized_quicksort(array_0)
    end_time = time.thread_time()
    print(f"Оптимизированная быстрая "
          f"сортировка заняла {end_time - start_time} секунд")
