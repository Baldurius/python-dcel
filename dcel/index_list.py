from __future__ import annotations
from typing import List, Any, Generic, TypeVar, Optional, Iterable, Iterator

ValueType = TypeVar('ValueType')


class IndexListIterator(Iterator[Optional[ValueType]]):
    def __init__(self, container: IndexList[ValueType]) -> None:
        self.__container = container
        self.__index: int = 0

    @property
    def index(self) -> int:
        return self.__index - 1

    def __next__(self) -> Optional[ValueType]:
        while True:
            if self.__index >= len(self.__container._elements):
                raise StopIteration

            self.__index += 1

            if self.__container._used[self.__index - 1]:
                return self.__container._elements[self.__index - 1]


class IndexList(Iterable[Optional[ValueType]]):
    def __init__(self) -> None:
        self._elements: List[Optional[ValueType]] = []
        self._used: List[bool] = []
        self.__indices: List[int] = []

    def push(self, value: Optional[ValueType] = None) -> int:
        if not self.__indices:
            self._elements.append(value)
            self._used.append(True)
            return len(self._elements) - 1
        else:
            index = self.__indices[-1]
            self.__indices.pop()
            self._elements[index] = value
            self._used[index] = True
            return index

    @property
    def size(self) -> int:
        return len(self._elements) - len(self.__indices)

    def __getitem__(self, index: int) -> Optional[ValueType]:
        return self._elements[index]

    def __setitem__(self, index: int,
                    value: Optional[ValueType]) -> Optional[ValueType]:
        self._elements[index] = value
        return value

    def __delitem__(self, index: int) -> None:
        self._elements[index] = None
        self._used[index] = False
        self.__indices.append(index)

    def __iter__(self) -> IndexListIterator[ValueType]:
        return IndexListIterator(self)
