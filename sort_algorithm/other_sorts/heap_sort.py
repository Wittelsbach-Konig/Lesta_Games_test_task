"""
Сортировка кучей.
"""


import random
import time
from typing import List


def heapify(array: List[int], n: int, i: int) -> None:
    """Функция для корректировки кучи.

    Args:
        array (List[int]): исходный массив
        n (int): длина массива
        i (int): индекс текущего узла
    """
    largest = i  # Инициализируем largest как корень
    lf = 2 * i + 1  # левый = 2*i + 1
    rg = 2 * i + 2  # правый = 2*i + 2

    # Если левый дочерний узел больше корня
    if lf < n and array[i] < array[lf]:
        largest = lf

    # Если правый дочерний узел больше, чем текущий largest
    if rg < n and array[largest] < array[rg]:
        largest = rg
    if largest != i:
        # меняем корень с лучшим дочерним узлом
        array[i], array[largest] = array[largest], array[i]
        # рекурсивно вызываем heapify на поддереве, где корень = largest
        heapify(array, n, largest)


def heap_sort(array: List[int]) -> None:
    """
    Сортировка кучей.

    Args:
        array (List[int]): исходный массив
    """
    n = len(array)
    # Построение max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Удаление элементов из max heap
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # перемещаем корень в конец
        heapify(array, i, 0)  # вызываем heapify на поддереве, где корень = 0


if __name__ == "__main__":
    array_0 = [random.randint(0, 100) for _ in range(100)]
    array_1 = list(range(100))
    start_time = time.thread_time()
    heap_sort(array_0)
    end_time = time.thread_time()
    print(f"Сортировка кучей на случайном массиве заняла "
          f"{end_time - start_time} секунд")
    start_time = time.thread_time()
    heap_sort(array_1)
    end_time = time.thread_time()
    print(f"Сортировка кучей на отсортированном массиве заняла "
          f"{end_time - start_time} секунд")
    print(array_0)
    print(array_1)
