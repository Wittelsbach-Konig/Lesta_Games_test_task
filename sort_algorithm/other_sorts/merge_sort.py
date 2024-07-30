"""
Сортировка слиянием.
"""


from typing import List


def merge_sort(arr: List[int]) -> None:
    """Функция сортировки слиянием.

    Args:
        arr (List[int]): массив для сортировки
    """
    if len(arr) > 1:
        # Находим середину списка
        mid = len(arr) // 2
        # Разделяем список на две половины
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем обе половины
        merge_sort(left_half)
        merge_sort(right_half)

        # Инициализируем индексы для обхода обеих половин
        i = j = k = 0

        # Объединяем отсортированные половины
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы из левой половины (если есть)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы из правой половины (если есть)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [4, 2, 1, 5, 3]
    merge_sort(arr)
    print(arr)  # Output: [1, 2, 3, 4, 5]
