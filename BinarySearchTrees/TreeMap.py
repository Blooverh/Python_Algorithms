"""Implementation of a sorted map using a Binary search tree"""
from TreesChpt import LinkedBinaryTree
from Maps_HashTables_SkipLists import MapBase

class TreeMap(LinkedBinaryTree, MapBase): #Multiple inheritance 
    
    class Position(LinkedBinaryTree.Position): #Inherits inner class of LinkedBinaryTree class
        def key(self):
            """return key of map's (key-value) pair"""
            return self.element()._key
        
        def value(self):
            """return value of map's (key-value) pair"""
            return self.element()._value
        
    # Private/ protected utilities
    def _subtree_search(self, p, k):
        """Return position of p's subtree having key k or last node searched"""

        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k) #recursively search left subtree
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k) #recursively search rigth subtree
            
        return p # last position searched from recursion if search not a success
    
    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p
        position with the least key from (sub)tree rooted at p, which is leftmost node (item) in Tree """
        walk = p
        while self.left(walk) is not None:
            walk= self.left(walk) 

        return walk
    
    def _subtree_last_position(self, p):
        """Return position of last item in (sub)tree rooted at p
        which is the right most item in the (sub)tree, since is 
        the position with largest key """
        
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)

        return walk
    
    def first(self):
        """Return the first position in the Tree or None if Tree is empty"""

        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    
    def last(self):
        """Return the last position in the Tree or None if Tree is empty"""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None
    
    def before(self, p):
        """Return the Position just before p in natural order
        return None if p does not have children (first position on subtree)"""

        self._validate(p) # inherited from LinkedBinaryTree, to validate if position p exists in Tree

        if self.left(p):
            # walk through left subtree of p until it recursively finds greatest key strictly less than p
            # since last key on left subtree of p have key with value right before key at p
            return self._subtree_last_position(self.left(p)) 
        else:
            #else walk upwards as the last key with no parent is the greatest key less than key at position p
            walk = p
            above = self.parent(walk)
            while above is not None and walk ==  self.left(above):
                walk = above 
                above =self.parent(walk)

            return above 
    
    def after(self, p):
        """Return the position just after p in the natural order
        
        Symmetric to before(p)"""

        self._validate(p) 

        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk= p 
            above = self.parent(walk)

            while above is not None and walk == self.right(above):
                walk =  above
                above = self.parent(walk)

            return above
        
    def find_position(self, k):
        """Return position with key k, or self neighbor or None if empty"""

        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # hook for balanced tree subclasses
            return p
        
    def find_min(self):
        """Return (k,v) pair with the minimum key is map"""

        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key, p.value)
    
    def find_ge(self, k):
        """Return (k,v) pair with least key greater than or equal to k
        Return None if there is not such key"""

        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
        
    def find_range(self, start, stop):
        """iterate through all items such that start <= key < stop
        if start is None, begin iteration with min key of map
        if stop is None, iterate until last key (max key in map)"""
        
        if not self.is_empty():
            if start is None:
                p = self.first
            else:
                p =  self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k
         if tree is empty raise error """
        
        if self.is_empty():
            raise KeyError("Key Error: "+ repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # hook for balanced tree subclasses
            if  k != p.key():
                raise KeyError("Key Error" + repr(k))
            return p.value()
        
    def __setitem__(self, k, v):
        """assign value v to key k if it exists, else make position """
        
        # if tree is empty add pair as root of the tree
        if self.is_empty():
            leaf= self._add_root(self._Item(k,v))
        else:
            p = self._subtree_search(self.root(), k)

            if k == p.key():
                p.element()._value = v
                self._rebalance_access(p)
                return 
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    leaf= self._add_right(p, item)
                else:
                    leaf =  self._add_left(p, item)
            
        self._rebalance_insert(leaf) 

    def __iter__(self):
        """Genrate iteration of all keys in the map in order """
        p = self.first() 
        while p is not None:
            yield p.key()
            p= self.after(p)

    def delete(self, p):
        """Remove item at position p"""

        self._validate(p)

        if self.left(p) and self.right(p):
            replacement =  self._subtree_last_position(p)
            self._replace(p, replacement.element()) # replaces Item at p with replacement item
            p = replacement 
            parent = self.parent(p)
            self._delete(p)
            self._rebalance_delete(parent) #if root deleted than parent is None, so we rebalance the tree

    def __delitem__(self, k):
        """Remove item associated with key k"""
        if not self.is_empty():
            p =  self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        
        raise KeyError("Key Error: "+ repr(k))
