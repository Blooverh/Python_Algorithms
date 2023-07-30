"""
Open addressing with linear probing. 
In order to support deletions, we place a special marker in a table location at 
which an item has been deleted, so that we can distinguish between it and a location 
that has always been empty

OPPEN ADDRESSING CHALLENGE:
    - properly trace the series of probes when collisions occur during an insertion or
    search for an item."""
import HashMapBase
class ProbeHashMap(HashMapBase):
    """HashMap implemented with linear probing for collision resolutions"""

    _AVAIL = object() #sentinel marks location of previous deletion

    def _is_available(self, j):
        """Return true if index j is available in the table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j ,k):
        """search for key k in bucket at index j
        
        Return (success, index) tuple, described as follow:
        If match was found, success is True and index denotes its location 
        If no match found, success is False and index denotes first available slots """

        firstAvail= None

        while True:
            if firstAvail is None:
                firstAvail = j #mark this as first available 
            
            if self._table[j] is None:
                return (False, firstAvail) #search has failed 
            elif k == self._table[j]._key:
                return (True , j) #found a match 
            
            j = (j+1) % len(self._table) #keep looking cyclically

    def _bucket_getitem(self, j ,k):
        found, s = self._find_slot(j, k) #find slot at bucket j the key k to retrieve the Item

        if not found:
            raise KeyError("Key Error" + repr(k)) #no match found
        
        return self._table[s]._value #return the element at position s of the hashtable 

    def _bucket_setitem(self, j, k, v):
        found, s =  self._find_slot(j,k) #find at bucket j the key k 

        if not found:
            self._table[s] = self._Item(k,v) #insert new item
            self._n +=1 # increase size 
        else:
            self._table[s]._value= v #overwrite existing

    def _bucket_delitem(self, j , k):
        found, s = self._find_slot(j,k) # find slot in j with key k to delete 

        if not found:
            raise KeyError("Key error" + repr(k))

        self._table[s] = ProbeHashMap._AVAIL #mark slot as vacated after deletion

    def __iter__(self):
        for j in range(len(self._table)): # Scan the entire table
            if not self._is_available(j):
                yield self._table[j]._key # yields every key in hashtable when iterating