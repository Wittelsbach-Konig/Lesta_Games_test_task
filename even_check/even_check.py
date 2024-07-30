"""
Алгоритм определения четности целого числа, с помощью битовых операций.

Автор: Кирюшин Виталий
"""


def is_even(n: int) -> bool:
    """
    Функция проверяет является ли целое число чётным.

    Args:
        n (int): целое число проверяемое на чётность

    Returns:
        bool:  true если чётное, false если нечётное.
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом!")
    return n & 1 == 0
