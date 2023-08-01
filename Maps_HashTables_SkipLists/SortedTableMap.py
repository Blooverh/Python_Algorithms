import MapBase

class SortedTableMap(MapBase):
    """Map implementation using a sorted Table"""

    #Protected / Private methods
    def _find_index(self, k, low, high):
        """Uses the Binary search algorithm and returns the index of the target key,
        if item does not exist return index of item is max key
        
        Return index of the left most item with key greater than or equal to k
        
        return high + 1 if no such item qualifies (item with max key in this case)
        
        That is j will be return such that:
        all items of slice  table[low: j] have key < k
        all items of slice table[j: high+1] have key >= k
        """

        if high < low:
            return high + 1 #if no key qualifies return index of item with max key
        else:
            #perform binary search
            mid= (high+low) //2 
            if k == self._table[mid]:
                return mid
            elif k < self._table[mid]:
                self._find_index(k, low, mid-1)
            else:
                self._find_index(k, mid+1, high)

    # ---------- Public Methods --------------
    def __init__(self):
        """create an empty map as array based sequence (list)"""
        self._table=[]

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)
    
    def __getitem__(self, k):
        """Return index of (key,value) where k = key, Raise Error if key not found"""

        j =  self._find_index(self._table, k, 0, len(self._table)-1) # perform binary search for look up and store in j

        # if index j is the last index of map or no item in map contains the key at a certain index raise error
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error: " + repr(k)) 
        
        return self._table[j]._value # return value assciated with key k if at index j there is a k == key of item at j
    
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existin value if another value is present at target k"""
        j = self._find_index(k, 0, len(self._table)-1) 

        if j < len(self._table) and self._table[j]._key == k: # index j that has key == to target k must be less than length of map
            self._table[j]._value = v #swap value if item with key k already has a value
        else:
            self._table.insert(j, self._Item(k,v)) # Add new item at position j

    def __delitem__(self, k):
        """Remove Item associated with key k (raise error if key not found in map)"""
        j = self._find_index(k, 0, len(self._table)-1)

        if j == len(self._table) or self._table[j]._key != k: #if no item has key k for any index j or j is last element in map
            raise KeyError("Key Error" + repr(k))  #raise error as key does not exist in map
        
    def __iter__(self):
        """Generate keys of the mpa ordered from minimum to maximum key"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map from maximum to minimum"""
        for item in reversed(self._table):
            yield item._key 
    
    def find_min(self):
        """Return the item (k,v) where k is the minimum key in map or None if map is empty"""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            None

    def find_max(self):
        """Return item (k,v) where k is the maximum key in map or None if map is empty"""
        if len(self._table)>0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
        
    def find_ge(self, k):
        """return (k,v) pair with least key greater than or equal to k"""
        j = self._find_index(k, 0, len(self._table)-1) # j's key >= k

        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
             return None
        
    def find_lt(self, k):
        """return (k,v) pair with greatest key strictly smaller than k"""
        j = self._find_index(k, 0, len(self._table)-1)

        if j < len(self._table):
            return (self._table[j-1]._key, self._table[j-1]._value) # j-1 since is greatest key < than k
        else:
            return None
        
    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self. table) - 1)

        if j < len(self._table) and self._table[j]._key == k:
            j+=1
        
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    
    def find_range(self, start, stop):
        """Iterate through all the (k,v) pairs such that start <= key < stop
        
        if start is None, iterate from item with minimum key until stop
        if stop is None, iterate from item at start until the end of the map
        """

        if start is None:
            j=0
        else:
            j = self._find_index(start, 0, len(self._table) -1) #find result
        
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j+=1