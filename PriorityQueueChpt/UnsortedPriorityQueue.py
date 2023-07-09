from queue import Empty
import PriorityQueue
from LinkedLists import PositionalList 
# We use multiple inheritance since this ADT needs both the priorityQueue and Positional list super classes

class UnsortedPriorityQueue(PriorityQueue, PositionalList): 
    """A min_oriented priotity queue implemented with an unsorted list"""

    #private method
    def _find_min(self):
        """Return Position of item with minimum key"""  
        if self.is_empty():
            raise Empty('priority queue is empty')
        
        small= self._data.first() 
        walk=self._data.after(small)

        while walk is not None: 
            if walk.element() < small.element():
                small=walk
            
            walk= self._data.after(walk)
        
        def __init__(self):
            self._data= PositionalList() 
        
        def __len__(self):
            return len(self._data)
        
        def add(self, key, value):
            """Add a key-value pair"""
            self._data.add_last(self._Item(key, value))

        def min(self):
            """Return but to not remove the element with the minimum key"""
            p=self._find_min()
            item= p.element()
            return (item._key, item._value)
        
        def remove_min(self):
            """Remoave and returb the (k,v) pair item with the minimum key"""
            p= self._find_min()
            item=self._data.delete(p)
            return (item._key, item._value)
