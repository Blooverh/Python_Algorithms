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
        raise NotImplementedError()