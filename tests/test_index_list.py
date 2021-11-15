import os
import sys
sys.path.insert( 0, os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..' ) ) )

from dcel.index_list import IndexList

import pytest


def test_index_list():
    index_list = IndexList()

    # Push new element
    assert 0 == index_list.push()
    assert 1 == index_list.size

    # Set the element
    index_list[ 0 ] = 5
    assert 5 == index_list[ 0 ]

    # Push another element
    assert 1 == index_list.push()
    assert 2 == index_list.size

    # Remove one element
    del index_list[ 0 ]
    assert 1 == index_list.size

    # Push and re-use slot
    assert 0 == index_list.push()
    assert None == index_list[ 0 ]
