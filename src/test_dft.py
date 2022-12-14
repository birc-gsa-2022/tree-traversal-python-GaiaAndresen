# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from tree import T
from dft import in_order


def test_in_order() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(in_order(tree))
    assert res == [1, 2, 3, 4, 5]
    assert list(in_order(None)) == []

    tree = T(4, T(2, T(1, None, None), T(3, None, None)), T(6, T(5, None, None), T(7, None, None)))
    res = list(in_order(tree))
    assert res == [1, 2, 3, 4, 5, 6, 7]

    tree = T(1, None, None)
    res = list(in_order(tree))
    assert res == [1]

    tree = T(4, T(2, T(1, None, None), T(3, None, None)), None)
    res = list(in_order(tree))
    assert res == [1, 2, 3, 4]

    tree = T(4, T(1, None, T(3, T(2, None, None), None)), None)
    res = list(in_order(tree))
    assert res == [1, 2, 3, 4]


    tree = T(0, None, None)
    res = list(in_order(tree))
    assert res == [0]

    tree = T(0, T(1, None, None), T(0, None, None))
    res = list(in_order(tree))
    assert res == [1, 0, 0]

    tree = T(0, T(0, None, None), T(0, None, None))
    res = list(in_order(tree))
    assert res == [0, 0, 0]

    tree = T(0, T(0, T(0,None,None), None), T(0, None, None))
    res = list(in_order(tree))
    assert res == [0, 0, 0, 0]