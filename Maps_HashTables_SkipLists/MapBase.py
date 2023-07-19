from collections import MutableMapping

class MapBase(MutableMapping):
    """Our own ADT class that includes nonpublic _Item class"""
    
    # NESTED ITEM CLASS
    class _Item:
        """Lightweight composite to store (k,v) pairs as map items"""

        __slots__ = 'key', 'value'
        def __init__(self, k, v): #constructor
            self._key = k
            self.value = v
        
        def __eq__(self, other):
            return self._key == other._key #compare items based on their keys
        
        def __ne__(self, other):
            return not (self == other) # opposite of __eq__
        
        def __lt__(self, other):
            return self._key < other._key #compare items based on their keys 
        
    """Extending the MutableMapping abstract base class to provide a nonpublic _Item class
    for use in our various map implementations"""