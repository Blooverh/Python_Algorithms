import Tree
class BinaryTree(Tree):
    """Abstract class representing a Binary tree"""

    #Additional abstract methods only used by binary trees

    def left(self, p):
        """return a position representing p's left child
        return None if p does not have a left child """

        raise NotImplementedError("must be implemented by the subclass")
    
    def right(self, p):
        """Return a position representing p's right child 
        return None if p does not have a left child """

        raise NotImplementedError("Must be implemented by the subclass")
    
    def sibling(self, p):
        """Return a position representing p's sibling
        return None if no sibling since it can be a root or a leaf with no sibling"""

        parent= self.parent(p)

        if parent is None:
            return None
        
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Genrate an iteration of positions representing p's children """

        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)

    