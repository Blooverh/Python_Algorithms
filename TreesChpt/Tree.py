class Tree:
    """Abstract base class representing a tree struct."""

    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, other):
            """Return true if other Position represents the same location"""
            raise NotImplementedError("must be implmemented by subclass")
        
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self == other)
        

    # Abstract methods that concrete subclass must support 
    def root(self):
        """Return Position representing the root of tree or (None if empty tree)"""
        raise NotImplementedError("Must be implemented by the subclass")
    
    def parent(self):
        """Return the position representing the parent of node at position p
        or none if empty"""
        raise NotImplementedError("Must be implemented by subclass")
    
    def num_children(self, p):
        """Return the number of children that position p has"""
        raise NotImplementedError("Must be defined by subclass")
    
    def children(Self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("Must be implemented by the subclasss")
    
    def is_root(self, p):
        """Return boolean value on whether node at position p is the root of the
        tree"""

        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if position p does not have any children, meaning
        both left and right child nodes of node at p have value None"""

        return self.num_children(p)==0
    
    def is_empty(self):
        """Return True if the tree  is empty"""
        return len(self) == 0
    
    """Calculating the depth of a element at p"""
    def depth(self, p):
        """Return the number of levels separating position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1+ self.depth(self.parent(p))
        
    """Relies on top down fashion"""
    def _height2(self, p):
        """Return the height of the subtree rooted at position p"""
        if self.is_leaf(p):
            return 0 
        else: 
            return 1 + max(self._height(c) for c in self.children(p))
        
    def height(self, p=None):
        """Return the height of the subtree rooted at position p
        if p is None, return the height of the entire tree """

        if p is None:
            p=self.root()
        
        return self._height2(p)