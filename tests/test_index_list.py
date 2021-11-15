import _paths
from dcel.index_list import IndexList

import pytest


def test_index_list() -> None:
    index_list: IndexList[int] = IndexList()

    # Push new element
    assert 0 == index_list.push()
    assert 1 == index_list.size

    # Set the element
    index_list[0] = 5
    assert 5 == index_list[0]

    # Push another element
    assert 1 == index_list.push()
    assert 2 == index_list.size

    # Remove one element
    del index_list[0]
    assert 1 == index_list.size

    # Push and re-use slot
    assert 0 == index_list.push()
    assert index_list[0] is None


def test_index_list_iteration() -> None:
    VALUES = [1, 3, 23, 65, 0, -4, -4]

    index_list: IndexList[int] = IndexList()

    for value in VALUES:
        index_list.push(value)

    assert [value for value in index_list] == VALUES

    del index_list[0]
    del index_list[-1]

    assert [value for value in index_list] == VALUES[1:-1]
