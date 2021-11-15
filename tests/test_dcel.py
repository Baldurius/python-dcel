import _paths
from dcel import Dcel


def test_dcel() -> None:
    dcel = Dcel()

    edge = dcel.add_edge()
    node = dcel.add_node()

    edge.node = node
    node.edge = edge

    assert edge == node.edge
