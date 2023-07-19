import MapBase

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list"""
    def __init__(self):
        """create an empty map"""
        self._table=[] #list of items

    def __getitem__(self, k):
        """Return value associated with key k (raise keyError if not found)"""
        for item in self._table:
            if k == item._key:
                return item._key
        
        raise KeyError('KeyError: '+ repr(k))
    
    def __setitem__(self, k, v):
        """Assign a key-value pair to the map overwriting existing value if present"""

        for item in self._table:
            if k == item._key:
                item._value = v 
                return
        
        #did not find match for key
        self._table.append(self._Item(k,v))
    
    def __delitem__(self, k):
        """Remove item associated with key k (raise key error if key not in map)"""

        for i in range(len(self._table)):
            if k == self._table[i]._key:
                self._table.pop(i)
                return
            
        raise KeyError("Key Error" + repr(k))
    
    def __len__(self):
        """return number of items in the map"""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys"""
        for item in self._table:
            yield item._key