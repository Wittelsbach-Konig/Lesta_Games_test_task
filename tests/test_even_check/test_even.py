import pytest

from even_check.even_check import is_even


def test_valid_even(even_number):
    assert is_even(even_number)


def test_fail_odd(odd_number):
    assert not is_even(odd_number)


def test_invalid_type():
    with pytest.raises(TypeError):
        is_even("not a number")
