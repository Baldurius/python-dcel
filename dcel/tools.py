from . import dcel


def merge_regular_node(node: dcel.Node) -> None:
    """
    Remove a regular node by rerouting incident edges to connect its
    neighbors.

    :param node: Regular node to remove from the corresponding DCEL
    """

    # A regular node has to have degree 2
    assert node.degree == 2

    # Get both outgoing edges
    e1 = node.edge
    e2 = e1.twin.nxt

    # Reconnect incoming edges
    e1.twin.twin = e2.twin
    e2.twin.twin = e1.twin

    e1.twin.nxt = e2.nxt
    e2.twin.nxt = e1.nxt

    e1.nxt.prv = e2.twin
    e2.nxt.prv = e1.twin

    # Delete outgoing edges and regular node
    e1.remove()
    e2.remove()
    node.remove()
