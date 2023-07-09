class PriorityQueue:
    """ADT base class for a priority queue"""

    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key=k
            self._value=v

        #Compares items based on their keys
        def __lt__(self, other):
            return self._key < other._key
        
    
    def is_empty(self):
        """Return True if priority queue does not have any items stored"""
        return len(self) == 0
        