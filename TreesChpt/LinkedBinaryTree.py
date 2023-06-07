import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""

            self._container=container
            self._node= node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            """return true is other is a position representing the same location as node"""
            return type(other) is type(self) and other._node is self._node
        
        def _validate(self, p):
            """Return associated node if position is valid """
            if not isinstance(p, self.Position):
                raise TypeError("p must be proper Position Type")
            
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            
            if p._node._parent is p._node:
                raise ValueError("p is no longer valid")
            
            return p._node
        
        def _make_position(self, node):
            """Return position instance for given node of none if no node"""
            return self.Position(self, node) if node is not None else None
        
    #### BINARY TREE CONSTRUCTOR 

    def __init__(self):
        self._root=None
        self._size=0

    ### Public accessors 
    def __len__(self):
        """return the total number of elements in the tree"""
        return self._size
    
    def root(self):
        """return the root position of the tree or none if tree is empty"""
        return self._make_position(self._root)
    
    def parent(self, p):
        """return the position of p's parent or none if no parent"""
        node= self._validate(p) # validate if p is a position containing a node 
        return self._make_position(node._parent)
    
    def left(self, p):
        """return the position of p's left child or none if no left child"""
        node= self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node= self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self,p):
        node= self._validate(p)

        count=0

        """increment count if left node exists"""
        if node.left is not None:
            count +=1 
        """increment count if right node exists"""        
        if node.right is not None:
            counr+=1

        return count 
    

    def _add_root(self, e):
        """place element e at the root of an empty tree and return new Position
        raise ValueError if Tree is not empty"""
        if self._root is not None:
            raise ValueError("Tree is not empty, so we cannot add element e")
        
        self._size=1

        self._root=self._Node(e)

        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """place element e at the left of parent node or raise value Error if already has left child"""
        node =self._validate(p)

        if node._left is not None: raise ValueError("left child already exists")

        self._size+=1
        self._left=self._Node(e)

        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        node= self._validate(p)
        if node._right is not None:
            raise ValueError("right child already exists")
        
        self._size+=1
        self._right=self._Node(e)

        return self._make_position(node._right)
    
    def _replace(self, p, e):
        node= self._validate(p)

        if node is None:
            raise ValueError("The node is empty")
        
        old= node._element
        node._element=e

        return old
    
    def _delete(self, p):
        """Delete node at Position p, and replace it with its child, if any
        return the deleted element at position p
        raise value error if position p is invalid or p has 2 children"""

        node= self._validate(p)
        if self.num_children(p)  == 2:
            raise ValueError("node at p has 2 children")
        child= node._left if node._left else node._right #check which child is Null 

        if child is not None:
            child._parent = node._parent #child's grand parent becomes the parent

        if node is self._root:
            self._root= child # if deleted node is root its child becomes the root 
        else:
            parent= node._parent # parent is child's grandparent now
            if node is parent._left: # if node is left node of grand parent
                parent._left=child # child becomes now the child of the grand parent 
            
            else:
                parent._right=child 
        
        self._size -=1 
        node._parent= node #convention for deprecated node

        return node._element
    
    def _attach(self, p, T1, T2):
        """Attach Tree1 and Tree2 as left and right subtrees of external p"""

        node= self._validate(p)

        if not self.is_leaf(p):
            raise ValueError("node at p is not a leaf of tree")
        
        if not type(self) is type(T1) is type(T2):
            raise ValueError("Tree types must match")
        
        self._size= len(T1) + len(T2)

        if not T1.is_empty(): # attach T1 as left subtree of node at p
            T1._root._parent=node
            node._left = T1._root
            T1._root= None #root of T1 is now None since new root, is leaf p
            T1._size= 0 #set size of T1 to 0 after attachment to Tree

        if not T2.is_empty():
            T2._root._parent=node
            node._right= T2._root
            T2.root= None
            T2._size=0