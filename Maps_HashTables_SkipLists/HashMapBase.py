from random import randrange
import MapBase

class HashMapBase(MapBase):
    """ADT class for map using Hash-Tables with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hashtable map
        cap - capacity 
        p - positive prime numbver used for MAD by default """

        self._table=cap * [None] # creates an empty list containing 11 entries of value None
        self._n=0 # no items present in the list; number of entries is 0 by default
        self._prime= p
        self._scale = 1 + randrange(p-1) #scale from 1 to p-1 for MAD picks a random number
        self._shift = randrange(p) #shift from 0 to p-1 for MAD

    def _hash_function(self, k): 
        """Performs Python's built in calaulation for creating the hashcode of a key 
        hash_function(k) """

        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)
    
    def __length__(self):
        return self._n #returns the number of distinct items present in the table at the time of method call. 
    
    def __getitem__(self, k):
        j = self._hash_function(k) # j holds hash code of the key k 

        return self,self._bucket_getitem(j, k) # may raise key error if hashcode does not exist for a key k
    
    def __Setitem__(self, k,v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v) #sub routine maintains self._n
        # increase n if item is added to hashtable 
        if len(self._table) // 2 < self._n: # keep load factor of hash table under 0.5, if surpasses 
            self._resize(2 * len(self._table) -1 ) #resise table by creating a new table double the size
            # 2 * x - 1 is often a prime number
    def __delitem__(self, k):
        j= self._hash_function(k) 
        self._bucket_delitem(j, k) #may raise key error if hashcode does not match to the key k
        self._n -=1 # decrease number of items
    
    def _resise(self, c):
        """if load factor passes 0.5 create a new table with capacity c size as long as that capacity c 
        will have the load factor under 0.5 and copy all items to the new table
        This is done to keep the load factor under or equal to 0.5 for better collision handling."""

        old=list(self.items()) # use iteration to record existing items 
        self._table = c * [None] # reset table to desirable capacity 
        self._n = 0 # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v #reinsert old key-value pair into resized table