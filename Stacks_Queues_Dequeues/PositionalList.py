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
    
    def _make_position(self, node):
        """Return position instance for given node or None if sentinel """
        if node is self._header or node is self._trailer:
            return None  #  boundary violation
        else:
            return self.Position(self, node) #legitimate position not based on the sentinels 
        
    # ACCESSORS

    def first(self):
        """Return 1st position in the list or None is list is empty """
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the position just before position p or None is p is first"""
        node = self._validate(p) # validate the position p if node before position p exists return true else false

        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the position just adter position p unless its None and p is the last position"""
        node = self._validate(p)

        return self._make_position(node._next)
    
    def __iter__(self):
        """Generates a forward iteration if the elements of the list"""
        cursor= self.first()

        while cursor is not None: 
            yield cursor.element()
            cursor=self.after(cursor)
    
    #MUTATORS 
    
    #Override inherited version to return Position rather than node when adding node in between the list
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes"""
        node = super()._insert_between(e, predecessor, successor)

        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element at front of the list and return new position"""
        return self._insert_between(e, self._header, self._header._next) 
    
    def add_last(self, e):
        """Inser element at end of the list and return new position """
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before position P and return new position"""
        original= self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after position p and return new position"""
        original=self._validate(p)

        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Delete node at a position p and return node"""
        original= self._validate(p)
        return self._delete._node(original)

    def replace(self, p, e):
        """Replace element at position p with element e and return the old element at position p"""
        original= self._validate(p)
        old_value= original._element
        original._element=e

        return old_value

