"""Testing breadth-first traversal"""

from tree import T
from bft import bf_order


def test_in_order() -> None:
    """Test in_order. Add tests as needed."""
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    res = list(bf_order(tree))
    assert res == [2, 1, 4, 3, 5]
    assert list(bf_order(None)) == []

    tree = T(1, None, None)
    res = list(bf_order(tree))
    assert res == [1]

    tree = T(1, T(2, None, T(3, None, None)), None)
    res = list(bf_order(tree))
    assert res == [1, 2, 3]

    tree = T(0, None, None)
    res = list(bf_order(tree))
    assert res == [0]

    tree = T(0, T(1, None, None), T(0, None, None))
    res = list(bf_order(tree))
    assert res == [0, 1, 0]
