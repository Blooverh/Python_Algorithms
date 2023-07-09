from queue import Empty
import PriorityQueue

from LinkedLists import PositionalList

class SortedPriorityQueue(PriorityQueue, PositionalList):
    """A min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        """create a new empty Priority Queue"""
        self._data= PositionalList()

    def __len__(self):
        """Return the amount of items that are in the priority queue"""
        return len(self._data)
    
    def add(self, key, value):
        """Add a Key-Value pair"""
        newest=self._Item(key, value) #make a new item instance
        walk= self._data.last() # walk backwards looking for smaller key

        while walk is not None and newest < walk.element():
            walk= self._data.before(walk)
            if walk is None:
                self._data.add_first(newest) #new key is the smallest
            else:
                self._data.add_after(walk, newest) # newest goes after walk if newest > walk
    
    def min(self):
        """return a (k,v) tuple of the item with minimum key
        but do not remove instance from priority queue"""

        if self.is_empty():
            raise Empty('priority queue is empty')
        
        p= self._data.first()
        item= p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return a (k,v) tuple with the minimum value from the
        priority queue"""
        if self.is_empty():
            raise Empty('priority queue is empty')  
        
        p=self._data.first()
        item= self._data.delete(p)
        return (item._key, item.value)