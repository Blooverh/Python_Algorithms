from queue import Empty
import PriorityQueue

class Heap(PriorityQueue):
    """A min-oriented priority queue implemented with a binary heap"""

    #Non public methods (behaviors)
    def _parent(self, j):
        return (j-1)//2
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j): #index beyond list length

        return self._left(j) < len(self._data)
    
    def _has_right(self, j): #index beyond list length

        return self._right(j) < len(self._data)
    
    def _swap(self, i, j ):
        """Swap elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent= self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) #recursion at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left=self._left(j)
            small_child=left #although right may be smaller

            if self._has_right(j):
                right=self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child) #recursion at position of small child

    ### Public Methods Behaviors ###

    def __init__(self, contents=()):
        # self._data=[] no bottom-up heapify heap implementation
        """below implementation is for the bottom-up heap construction""" 
        self._data=[self._Item(k,v) for k,v in contents]
        if len(self._data) > 1:
            self._heapify()
    
    def _heapify(self):
        start = self._parent(len(self)-1) #start at parent of last leaf
        for j in range(start, -1, -1): #going to and including the root
            self._downheap(j)

    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        """Add key bvalue pair to priority queue """
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data)-1) #up-heap newly added position

    def min(self):
        """Return but do not remove key-value paior from priority queue with minimum key
        raise exception is empty"""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        
        item=self._data[0]
        return (item._key, item._value) 
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key
        raise empty exception if priority queue is empty"""

        if self.is_empty():
            raise Empty("Priority queue is empty")
        self.swap(0, len(self._data)-1) #put minimum item at end of the list
        item=self._data.pop() #remove it from the list 
        self._downheap(0) #then fix new root

        return (item._key, item._value)