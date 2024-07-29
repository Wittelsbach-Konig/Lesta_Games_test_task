class TestListBuffer:
    """Тесты буффера, реализованного на листе."""

    def test_push_pop_list(self, buffer_list):
        buffer_list.push(10)
        buffer_list.push(20)

        assert buffer_list.pop() == 10
        buffer_list.push(30)
        buffer_list.push(40)
        buffer_list.push(50)

        assert buffer_list.pop() == 20
        assert buffer_list.pop() == 30
        assert buffer_list.pop() == 40
        assert buffer_list.pop() == 50

    def test_peek_list(self, buffer_list):
        buffer_list.push(10)
        buffer_list.push(20)
        assert buffer_list.peek() == 10
        buffer_list.pop()
        buffer_list.push(30)
        assert buffer_list.peek() == 20
        buffer_list.push(40)
        buffer_list.push(50)
        assert buffer_list.peek() == 20

    def test_vaild_is_full(self, buffer_list):
        assert not buffer_list.is_full
        buffer_list.push(10)
        assert not buffer_list.is_full
        buffer_list.push(20)
        assert not buffer_list.is_full
        buffer_list.push(30)
        assert not buffer_list.is_full
        buffer_list.push(40)
        assert buffer_list.is_full

    def test_vaild_is_empty(self, buffer_list):
        assert buffer_list.is_empty
        buffer_list.push(10)
        assert not buffer_list.is_empty
        buffer_list.pop()
        assert buffer_list.is_empty


class TestDequeBuffer:
    """Тесты буффера, реализованного на deque."""

    def test_push_pop_deque(self, buffer_deque):
        buffer_deque.push(10)
        buffer_deque.push(20)
        assert buffer_deque.pop() == 10
        buffer_deque.push(30)
        buffer_deque.push(40)
        buffer_deque.push(50)

        assert buffer_deque.pop() == 20
        assert buffer_deque.pop() == 30
        assert buffer_deque.pop() == 40
        assert buffer_deque.pop() == 50

    def test_peek_deque(self, buffer_deque):
        buffer_deque.push(10)
        buffer_deque.push(20)
        assert buffer_deque.peek() == 10
        buffer_deque.pop()
        buffer_deque.push(30)
        assert buffer_deque.peek() == 20
        buffer_deque.push(40)
        buffer_deque.push(50)
        assert buffer_deque.peek() == 20

    def test_vaild_is_full(self, buffer_deque):
        assert not buffer_deque.is_full
        buffer_deque.push(10)
        assert not buffer_deque.is_full
        buffer_deque.push(20)
        assert not buffer_deque.is_full
        buffer_deque.push(30)
        assert not buffer_deque.is_full
        buffer_deque.push(40)
        assert buffer_deque.is_full

    def test_valid_is_empty(self, buffer_deque):
        assert buffer_deque.is_empty
        buffer_deque.push(10)
        assert not buffer_deque.is_empty
        buffer_deque.pop()
        assert buffer_deque.is_empty
