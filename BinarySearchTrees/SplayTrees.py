import TreeMap

class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree"""

    def _splay(self, p):

        while p != self.root():
            parent = self.parent(p) # y is parent of x 
            grand = self.parent(parent) # z is parent of y

            if grand is None:
                # if there is no z (grand father)
                # zig-zag case
                self._rotate(p) # from treeMap class 
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # zig-zig case 
                self._rotate(parent) # move parent up
                self._rotate(p) # move child p (x) up to the root
            else:
                #zig-zag case 
                self._rotate(p) #  move p up
                self._rotate(p) #move p up again

    ##### OVERRIDE BALANCING HOOKS #######
    def _rebalance_insert(self,p):
        self._splay(p)
    
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)