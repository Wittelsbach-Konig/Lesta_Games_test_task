"""
Тестирование сортировок.

Автор: Кирюшин Виталий
"""


import random
import numpy as np
import sys
import matplotlib.pyplot as plt
import pathlib

from time import thread_time
from typing import List, Callable, Dict

from sort_algorithm.optimized_quick_sort import optimized_quicksort
from sort_algorithm.other_sorts.basic_quick_sort import quicksort
from sort_algorithm.other_sorts.merge_sort import merge_sort
from sort_algorithm.other_sorts.heap_sort import heap_sort

sys.setrecursionlimit(10**9)  # Максимальная глубина рекурсии
TEST_COUNT = 20  # Количество запусков для каждого теста
ARRAY_TYPE = ("Случайный массив",
              "Частично отсортированный массив",
              "Отсортированный массив")  # Типы массивов
BASE_DIR = pathlib.Path(__file__).resolve().parent


def generate_random_array(length: int, min_value: int,
                          max_value: int) -> List[int]:
    """Функция генерации массива случайных чисел.

    Args:
        length (int): длина массива
        min_value (int): минимальное значение числа
        max_value (int): максимальное значение числа

    Returns:
        List[int]: массив случайных чисел
    """
    return [random.randint(min_value, max_value) for _ in range(length)]


def generate_partially_sorted_array(length: int) -> List[int]:
    """Функция генерации частично отсортированного массива.

    Args:
        length (int): длина массива

    Returns:
        List[List]: частично отсортированный массив
    """
    array = list(range(length))
    for i in range(length // 10):
        i1 = random.randint(0, length - 1)
        i2 = random.randint(0, length - 1)
        array[i1], array[i2] = array[i2], array[i1]
    return array


def time_calculation(sort_func: Callable[[list[int]], list[int] | None],
                     array: List[int]) -> float:
    """Функция измерения времени сортировки.

    Args:
        sort_func (Callable[[list[int]], list[int] | None]): функция сортировки
        array (List[int]): массив для сортировки
    Returns:
        int: время сортировки в секундах
    """
    start_time = thread_time()
    sort_func(array)
    return thread_time() - start_time


def sort_testing() -> None:
    """Тестирование сортировок."""
    lengths = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
    # lengths = [10, 20, 30, 40, 100]

    algorithms = {
        "Обычная быстрая сортировка": quicksort,
        "Оптимизированная быстрая сортировка": optimized_quicksort,
        "Пирамидальная сортировка": heap_sort,
        "Сортировка слиянием": merge_sort,
    }

    results: Dict[str, Dict[str, List]] = {
        name: {array: [] for array in ARRAY_TYPE} for name in algorithms.keys()
    }

    for length in lengths:
        print(f"\nДлина массива: {length} .")

        random_array = generate_random_array(length, 0, length)
        for name, sort_algorithm in algorithms.items():
            times = []
            for _ in range(TEST_COUNT):
                array_copy = random_array.copy()
                times.append(time_calculation(sort_algorithm, array_copy))
            average_time = np.mean(times)
            results[name][ARRAY_TYPE[0]].append(average_time)
            print(f"{name} на случайном массиве: {average_time:.6f} секунд")

        partially_sorted_array = generate_partially_sorted_array(length)
        for name, sort_algorithm in algorithms.items():
            times = []
            for _ in range(TEST_COUNT):
                array_copy = partially_sorted_array.copy()
                times.append(time_calculation(sort_algorithm, array_copy))
            average_time = np.mean(times)
            (results[name][ARRAY_TYPE[1]].append(average_time))
            print(f"{name} на частично отсортированном массиве: "
                  f"{average_time:.6f} секунд")

        sorted_array = list(range(length))
        for name, sort_algorithm in algorithms.items():
            times = []
            for _ in range(TEST_COUNT):
                array_copy = sorted_array.copy()
                times.append(time_calculation(sort_algorithm, array_copy))
            average_time = np.mean(times)
            results[name][ARRAY_TYPE[2]].append(average_time)
            print(f"{name} на отсортированном массиве: "
                  f"{average_time:.6f} секунд")

    fig, axes = plt.subplots(1, 3, figsize=(18, 10))
    fig.suptitle("Сравнение алгоритмов сортировок")

    for i, array_type in enumerate(ARRAY_TYPE):
        axe = axes[i]
        for name in algorithms.keys():
            axe.plot(lengths, results[name][array_type], label=name)
        axe.set_xscale("log")
        axe.set_yscale("log")
        axe.set_title(array_type)
        axe.set_ylabel("Время (секунды)")
        axe.set_xlabel("Длина массива")
        axe.legend()
        axe.grid(True)

    plt.tight_layout()
    plt.savefig(BASE_DIR / "charts/sorts_comparison.png")


if __name__ == "__main__":
    sort_testing()
