from functions import add
from functions import divide


def test_add():
    assert 4 == add(2, 2)


def test_divide():
    assert 2 == divide(4, 2)

