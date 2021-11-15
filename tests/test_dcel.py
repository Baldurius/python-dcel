import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dcel import Dcel


def test_dcel():
    dcel = Dcel()

    edge = dcel.add_edge()
    node = dcel.add_node()

    edge.node = node
    node.edge = edge

    assert edge == node.edge
