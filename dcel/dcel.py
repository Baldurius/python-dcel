from __future__ import annotations
from dataclasses import dataclass
from .index_list import IndexList
from typing import Optional


@dataclass
class NodeData:
    edge: Optional[int] = None


@dataclass
class EdgeData:
    node: Optional[int] = None
    twin: Optional[int] = None
    prv: Optional[int] = None
    nxt: Optional[int] = None


class Node(object):
    def __init__(self, dcel: Dcel, index: int) -> None:
        self.__dcel = dcel
        self.__index = index

    def remove(self) -> None:
        del self.__dcel._nodes[self.__index]

    @property
    def dcel(self) -> Dcel:
        return self.__dcel

    @property
    def index(self) -> int:
        return self.__index

    @property
    def edge(self) -> Edge:
        assert self.__data.edge is not None
        return Edge(self.__dcel, self.__data.edge)

    @edge.setter
    def edge(self, edge: Edge) -> None:
        self.__data.edge = edge.index

    @property
    def edges(self) -> NodeEdgeIterator:
        return NodeEdgeIterator(self)

    @property
    def degree(self) -> int:
        return sum(1 for _ in self.edges)

    @property
    def __data(self) -> NodeData:
        return self.__dcel._nodes[self.__index]

    def __eq__(self, other):
        return self.__index == other.__index

    def __setitem__(self, key, value):
        setattr(self.__data, key, value)

    def __getitem__(self, key):
        return getattr(self.__data, key)

    def __delitem__(self, key):
        delattr(self.__data, key)


class Edge(object):
    def __init__(self, dcel: Dcel, index: int) -> None:
        self.__dcel = dcel
        self.__index = index

    def remove(self) -> None:
        del self.__dcel._edges[self.__index]

    @property
    def dcel(self) -> Dcel:
        return self.__dcel

    @property
    def index(self) -> int:
        return self.__index

    @property
    def node(self) -> Node:
        assert self.__data.node is not None
        return Node(self.__dcel, self.__data.node)

    @node.setter
    def node(self, node: Node):
        self.__data.node = node.index

    @property
    def twin(self) -> Edge:
        assert self.__data.twin is not None
        return Edge(self.__dcel, self.__data.twin)

    @twin.setter
    def twin(self, edge: Edge):
        self.__data.twin = edge.index

    @property
    def prv(self) -> Edge:
        assert self.__data.prv is not None
        return Edge(self.__dcel, self.__data.prv)

    @prv.setter
    def prv(self, edge: Edge):
        self.__data.prv = edge.index

    @property
    def nxt(self) -> Edge:
        assert self.__data.nxt is not None
        return Edge(self.__dcel, self.__data.nxt)

    @nxt.setter
    def nxt(self, edge: Edge):
        self.__data.nxt = edge.index

    @property
    def __data(self) -> EdgeData:
        return self.__dcel._edges[self.__index]

    def __eq__(self, other):
        return self.__index == other.__index

    def __setitem__(self, key, value):
        setattr(self.__data, key, value)

    def __getitem__(self, key):
        return getattr(self.__data, key)

    def __delitem__(self, key):
        delattr(self.__data, key)


class Dcel:
    def __init__(self) -> None:
        self._edges = IndexList()
        self._nodes = IndexList()

    def add_node(self) -> Node:
        index = self._nodes.push()
        self._nodes[index] = NodeData()
        return Node(self, index)

    def add_edge(self) -> Edge:
        index = self._edges.push()
        self._edges[index] = EdgeData()
        return Edge(self, index)

    @property
    def nodes(self):
        return NodeIterator(self)

    @property
    def edges(self):
        return EdgeIterator(self)

    def node(self, index: int) -> Node:
        return Node(self, index)

    def edge(self, index: int) -> Edge:
        return Edge(self, index)

    def _node_data(self, index: int) -> NodeData:
        return self._nodes[index]

    def _edge_data(self, index: int) -> EdgeData:
        return self._edges[index]


class NodeEdgeIterator:
    def __init__(self, node: Node) -> None:
        self.__node = node
        self.__edge = self.__node.edge

    def __iter__(self):
        return self

    def __next__(self):
        if self.__edge is None:
            raise StopIteration

        edge = self.__edge
        self.__edge = edge.twin.nxt

        if self.__edge == self.__node.edge:
            self.__edge = None

        return edge


class NodeIterator:
    def __init__(self, dcel: Dcel) -> None:
        self.__dcel = dcel
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.__index >= self.__dcel._nodes.max_index:
                raise StopIteration

            self.__index += 1

            if self.__dcel._nodes.is_valid(self.__index - 1):
                return Node(self.__dcel, self.__index - 1)


class EdgeIterator:
    def __init__(self, dcel: Dcel) -> None:
        self.__dcel = dcel
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.__index >= self.__dcel._edges.max_index:
                raise StopIteration

            self.__index += 1

            if self.__dcel._edges.is_valid(self.__index - 1):
                return Edge(self.__dcel, self.__index - 1)
