"""
Циклический буфер FIFO, реализованный с помощью списка.

Автор: Кирюшин Виталий
"""


from typing import List


class CyclicBufferList[T]:
    """
    Класс для создания циклического буфера FIFO на основе List.
    """

    def __init__(self, max_size: int) -> None:
        self.__buffer: List[T | None] = [None] * max_size
        self.__max_size: int = max_size
        self.__head = 0
        self.__tail = 0
        self.__current_size = 0

    def __len__(self):
        return self.__current_size

    @property
    def is_full(self) -> bool:
        """Проверка является ли буффер заполненным.

        Returns:
            bool: true если заполнен, false если нет.
        """
        return self.__current_size == self.__max_size

    @property
    def is_empty(self) -> bool:
        """Проверка является ли буффер пустым.

        Returns:
            bool: true если пуст, false если нет.
        """
        return self.__current_size == 0

    def pop(self) -> T | None:
        """Извлечение первого элемента из буффера."""
        if self.is_empty:
            raise Exception("Buffer is empty")
        value = self.__buffer[self.__head]
        self.__head = (self.__head + 1) % self.__max_size
        self.__current_size -= 1
        return value

    def push(self, value: T) -> None:
        """Добавление нового элемента в буффер."""
        if self.is_full:
            raise Exception("Buffer is full")
        self.__buffer[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__current_size += 1

    def peek(self) -> T | None:
        """Просмотреть содержимое начала буффера без удаления элемента."""
        if self.is_empty:
            raise Exception("Buffer is empty")
        return self.__buffer[self.__head]
