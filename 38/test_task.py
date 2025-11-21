import pytest

def is_sum_even(x: int, y: int) -> bool:
    return (x + y) % 2 == 0

@pytest.mark.parametrize(
    "x,y,expected",
    [
        # even + even → even
        (2, 4, True),
        (0, 0, True),
        (-4, 8, True),
        (100, 200, True),

        # odd + odd → even
        (1, 3, True),
        (5, 7, True),
        (-1, 1, True),

        # even + odd → odd
        (2, 1, False),
        (4, 3, False),
        (0, 1, False),
        (-2, 5, False),
        (7, 8, False),
    ],
    ids=[
        "even+even", "zero+zero", "neg_even+pos_even", "large_even",
        "odd+odd", "larger_odd", "neg_odd+pos_odd",
        "even+odd_1", "even+odd_2", "zero+odd", "neg_even+odd", "odd+even"
    ]
)
def test_is_sum_even(x, y, expected):
    assert is_sum_even(x, y) == expected