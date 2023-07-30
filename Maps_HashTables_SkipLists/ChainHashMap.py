import HashMapBase
import UnsortedTableMap
class ChainHashMap(HashMapBase):
    """Hash map implementation using Separate Chaining Collision handling"""

    def _bucket_getitem(self, j, k):
        bucket= self._table[j] #bucket is a list at position j 
        if bucket is None: #if bucket does not exist 
            raise KeyError("Key Error" + repr(k)) #no match found because bucket does not exist 
        
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None: 
            self._table[j] = UnsortedTableMap() # creates a new bucket (unsorted table) to the table 
        
        oldsize = len(self._table[j])

        self._table[j][k] = v #assign value to the key k on bucket j

        if len(self._table[j]) > oldsize: # if bucket at j is > then oldsize new element was inserted so increase n
            self._n +=1
    
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]

        if bucket is None: 
            """if bucket does not exist raise error"""
            raise KeyError("Key error" + repr(k))
        
        del bucket[k] # delete item with key k if key k exists in bucket j 
    
    def __iter__(self):
        """Iterator to retrieve keys in hashmap without deleting them"""
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key 