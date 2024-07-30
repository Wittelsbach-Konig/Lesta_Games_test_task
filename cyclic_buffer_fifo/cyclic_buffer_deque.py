"""
Циклический буффер FIFO, реализованный с помощью deque.

Автор: Кирюшин Виталий
"""


from collections import deque


class CyclicBufferDeque[T]:
    """
    Класс для создания циклического буфера FIFO на основе deque.
    """

    def __init__(self, max_size: int) -> None:
        self.__buffer: deque[T] = deque(maxlen=max_size)
        self.__max_size: int = max_size

    def __len__(self):
        return len(self.__buffer)

    @property
    def is_full(self) -> bool:
        """Проверка является ли буффер заполненным.

        Returns:
            bool: true если заполнен, false если нет.
        """
        return self.__len__() == self.__max_size

    @property
    def is_empty(self) -> bool:
        """Проверка является ли буффер пустым.

        Returns:
            bool: true если пуст, false если нет.
        """
        return self.__len__() == 0

    def pop(self) -> T | None:
        """Извлечение первого элемента из буффера."""
        if self.is_empty:
            raise Exception("Buffer is empty")
        return self.__buffer.popleft()

    def push(self, value: T) -> None:
        """Добавление нового элемента в буффер."""
        if self.is_full:
            raise Exception("Buffer is full")
        self.__buffer.append(value)

    def peek(self) -> T | None:
        """Просмотреть содержимое начала буффера без удаления элемента."""
        if self.is_empty:
            raise Exception("Buffer is empty")
        return self.__buffer[0]
