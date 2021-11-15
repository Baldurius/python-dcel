from __future__ import annotations
from dataclasses import dataclass
from .index_list import IndexList
from typing import Optional, Any


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
        data = self.__dcel._nodes[self.__index]
        assert data is not None
        return data

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Node) and self.__index == other.__index

    def __setitem__(self, key: Any, value: Any) -> None:
        setattr(self.__data, key, value)

    def __getitem__(self, key: Any) -> Any:
        return getattr(self.__data, key)

    def __delitem__(self, key: Any) -> None:
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
    def node(self, node: Node) -> None:
        self.__data.node = node.index

    @property
    def twin(self) -> Edge:
        assert self.__data.twin is not None
        return Edge(self.__dcel, self.__data.twin)

    @twin.setter
    def twin(self, edge: Edge) -> None:
        self.__data.twin = edge.index

    @property
    def prv(self) -> Edge:
        assert self.__data.prv is not None
        return Edge(self.__dcel, self.__data.prv)

    @prv.setter
    def prv(self, edge: Edge) -> None:
        self.__data.prv = edge.index

    @property
    def nxt(self) -> Edge:
        assert self.__data.nxt is not None
        return Edge(self.__dcel, self.__data.nxt)

    @nxt.setter
    def nxt(self, edge: Edge) -> None:
        self.__data.nxt = edge.index

    @property
    def __data(self) -> EdgeData:
        data = self.__dcel._edges[self.__index]
        assert data is not None
        return data

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Edge) and self.__index == other.__index

    def __setitem__(self, key: Any, value: Any) -> None:
        setattr(self.__data, key, value)

    def __getitem__(self, key: Any) -> Any:
        return getattr(self.__data, key)

    def __delitem__(self, key: Any) -> None:
        delattr(self.__data, key)


class Dcel:
    def __init__(self) -> None:
        self._edges: IndexList[EdgeData] = IndexList()
        self._nodes: IndexList[NodeData] = IndexList()

    def add_node(self) -> Node:
        index = self._nodes.push()
        self._nodes[index] = NodeData()
        return Node(self, index)

    def add_edge(self) -> Edge:
        index = self._edges.push()
        self._edges[index] = EdgeData()
        return Edge(self, index)

    @property
    def nodes(self) -> NodeIterator:
        return NodeIterator(self)

    @property
    def edges(self) -> EdgeIterator:
        return EdgeIterator(self)

    def node(self, index: int) -> Node:
        return Node(self, index)

    def edge(self, index: int) -> Edge:
        return Edge(self, index)


class NodeEdgeIterator:
    def __init__(self, node: Node) -> None:
        self.__node = node
        self.__edge: Optional[Edge] = self.__node.edge

    def __iter__(self) -> NodeEdgeIterator:
        return self

    def __next__(self) -> Edge:
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
        self.__iter = dcel._nodes.__iter__()

    def __iter__(self) -> NodeIterator:
        return self

    def __next__(self) -> Node:
        next(self.__iter)
        return Node(self.__dcel, self.__iter.index)


class EdgeIterator:
    def __init__(self, dcel: Dcel) -> None:
        self.__dcel = dcel
        self.__iter = dcel._edges.__iter__()

    def __iter__(self) -> EdgeIterator:
        return self

    def __next__(self) -> Edge:
        next(self.__iter)
        return Edge(self.__dcel, self.__iter.index)
