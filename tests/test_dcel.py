import _paths
from dcel import Dcel


def test_dcel() -> None:
    dcel = Dcel()

    edge = dcel.add_edge()
    node = dcel.add_node()

    edge.node = node
    node.edge = edge

    assert edge == node.edge


def test_dcel_node_iteration() -> None:
    dcel = Dcel()

    node_1 = dcel.add_node()
    node_2 = dcel.add_node()
    node_3 = dcel.add_node()

    assert [node.index for node in dcel.nodes] == [0, 1, 2]

    node_2.remove()

    assert [node.index for node in dcel.nodes] == [0, 2]


def test_dcel_edge_iteration() -> None:
    dcel = Dcel()

    edge_1 = dcel.add_edge()
    edge_2 = dcel.add_edge()
    edge_3 = dcel.add_edge()
    edge_4 = dcel.add_edge()

    assert [edge.index for edge in dcel.edges] == [0, 1, 2, 3]
