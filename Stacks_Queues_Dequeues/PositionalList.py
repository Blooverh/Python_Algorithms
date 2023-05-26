import DoublyLinkedList

class PositionalList(DoublyLinkedList):
    """Sequential contained of elements allowing positional access"""

    # Nested position class 

    class Position:
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container=container
            self._node=node

        def element(self):
            """Return element stored a this position"""

            return self._node._element
        
        def __eq__(self, other):
            """tests if position p and q refer to the same node containing same element"""
            """Return True is other is a position representing the same location"""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return true is other does not represent the same location"""
            return not (self== other) # opposite of __eq__
    
    # Utility method 

    def _validate(self,p):
        """Return position of node or raise exception if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        
        return p._node
