from functions import add
from functions import multiply
from functions import divide

# Use this format
def test_multiply():
    assert 4 == multiply(2, 2)


def test_add():
    assert 4 == add(2, 2)


def test_divide():
    assert 2 == divide(4, 2)

