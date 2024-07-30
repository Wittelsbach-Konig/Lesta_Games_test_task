import pytest
from typing import List

from sort_algorithm.optimized_quick_sort import (optimized_quicksort,
                                                 insertion_sort)
from sort_algorithm.other_sorts.basic_quick_sort import quicksort
from sort_algorithm.other_sorts.merge_sort import merge_sort
from sort_algorithm.other_sorts.heap_sort import heap_sort


def is_sorted(array: List[int]) -> bool:
    """Проверка является ли массив отсортированным."""
    return all(array[i] <= array[i+1] for i in range(len(array)-1))


def insert_sort(array: List[int]) -> None:
    insertion_sort(array, 0, len(array) - 1)


@pytest.mark.parametrize(
        "sort_func", [optimized_quicksort, quicksort,
                      insert_sort, merge_sort, heap_sort]
    )
def test_sorting_algorithms(sort_func):
    """Тесты сортировок."""
    array = []
    sorted_array = array.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)

    array = [1]
    sorted_array = array.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)

    array = [2, 4, 6, 2, 1]
    sorted_array = array.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)

    array = [1, 2, 3, 4, 5]
    sorted_array = array.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)

    array = [5, 4, 3, 2, 1]
    sorted_array = array.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)

    arr = [-3, -1, -7, 2, 5, 0, -2]
    sorted_array = arr.copy()
    sort_func(sorted_array)
    assert is_sorted(sorted_array)
