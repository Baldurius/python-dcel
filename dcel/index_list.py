class IndexList:
    pass


class IndexListIterator:

    def __init__( self, container ):
        self.__container = container
        self.__index = 0

    def __next__( self ):
        while True:
            if self.__index >= len( self.__container._elements ):
                raise StopIteration

            self.__index += 1

            if self.__container._used[ self.__index - 1 ]:
                return self.__container._elements[ self.__index - 1 ]


class IndexList:

    def __init__( self ) -> None:
        self._elements = []
        self._used = []
        self.__indices = []

    def push( self, value=None ) -> int:
        if not self.__indices:
            self._elements.append( value )
            self._used.append( True )
            return len( self._elements ) - 1
        else:
            index = self.__indices[ -1 ]
            self.__indices.pop()
            self._elements[ index ] = value
            self._used[ index ] = True
            return index

    def is_valid( self, index: int ) -> bool:
        return self._used[ index ]

    @property
    def max_index( self ) -> int:
        return len( self._elements )

    @property
    def size( self ) -> int:
        return len( self._elements ) - len( self.__indices )

    def __getitem__( self, index: int ):
        return self._elements[ index ]

    def __setitem__( self, index: int, value ):
        self._elements[ index ] = value
        return value

    def __delitem__( self, index: int ):
        self._elements[ index ] = None
        self._used[ index ] = False
        self.__indices.append( index )

    def __iter__( self ):
        return IndexListIterator( self )