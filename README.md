![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# Lesta_Games_test_task
Тестовое задание для **Lesta Games**. Требуется на Python:

    1. Написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. 
    Пример:
        def isEven(value):
            return value % 2 == 0

    2. Написать минимум по 2 класса реализовывающих циклический буфер FIFO.
    3. Предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).

## Особенности реализации

1. Проверка на четность была реализована с помощью побитового логического AND.
2. Было реализовано 2 класса циклического буфера: с использованием List и Deque.
3. Был предложен модифицированный алгоритм быстрой сортировки (Quick Sort). Построены графики для сравнения быстродействия разных алгоритмов сортировки на трёх группах массивов разной длины.

Подробное описание:
* [Проверка чётности](even_check/README.md)
* [Циклический буфер](cyclic_buffer_fifo/README.md)
* [Сортировка](sort_algorithm/README.md)

Для проверки соответствия кодстайлу использовался **flake8**, проверка аннотаций осуществлялась с помощью **mypy**, тесты написаны с помощью **pytest**.
## Установка
1. Склонировать репозиторий:
```bash
git clone git@github.com:Wittelsbach-Konig/Lesta_Games_test_task.git
cd Lesta_Games_test_task
```
2. Настроить виртуальное окружение
```bash
poetry install
poetry shell
```
Или:
```bash
python -m venv venv \
pip install requirements.txt \
source venv/bin/activate
```

## Построить графики сравнения алгоритмов
Находясь в виртуальном окружении:
```bash
python sort_testing.py
```
## Структура проекта
```bash
    ├── LICENSE
    ├── README.md
    ├── charts
    │   └── sorts_comparison.png
    ├── cyclic_buffer_fifo
    │   ├── README.md
    │   ├── __init__.py
    │   ├── cyclic_buffer_deque.py  <-- Буфер на deque
    │   └── cyclic_buffer_list.py   <-- Буфер на листе
    ├── even_check                  
    │   ├── README.md
    │   ├── __init__.py
    │   └── even_check.py           <-- Проверка на чётность
    ├── poetry.lock
    ├── pyproject.toml
    ├── setup.cfg
    ├── sort_algorithm
    │   ├── README.md
    │   ├── __init__.py
    │   ├── optimized_quick_sort.py <-- Улучшенная быстрая сортировка
    │   └── other_sorts
    │       ├── __init__.py
    │       ├── basic_quick_sort.py <-- Классическая быстрая сортировка
    │       ├── heap_sort.py        <-- Пирамидальная сортировка
    │       └── merge_sort.py       <-- Сортировка слиянием
    ├── sort_testing.py             <-- Построение графиков
    └── tests                       <-- Директория с тестами
        ├── __init__.py
        ├── test_cyclic_buffer
        │   ├── __init__.py
        │   ├── conftest.py
        │   └── test_buffer.py
        ├── test_even_check
        │   ├── __init__.py
        │   ├── conftest.py
        │   └── test_even.py
        └── test_sort_algorithm
            ├── __init__.py
            └── test_sort.py
```

