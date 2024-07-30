import pytest

from cyclic_buffer_fifo import cyclic_buffer_deque, cyclic_buffer_list


BUFFER_SIZE = 4


@pytest.fixture
def buffer_deque():
    return cyclic_buffer_deque.CyclicBufferDeque(max_size=BUFFER_SIZE)


@pytest.fixture
def buffer_list():
    return cyclic_buffer_list.CyclicBufferList(max_size=BUFFER_SIZE)
