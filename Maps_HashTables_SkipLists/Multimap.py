class MultiMap:
    """A multimap class built in upon the use of an underlying map for storage"""
    _MapType = dict #Map type; can be redefined by sub class

    def __init__(self):
        """create a new empty multimap instance"""
        self._map =  self._MapType() #create a map instance for storage 
        self._n =0

    def __iter__(self):
        """Iterate through all (k,v) pairs in multimap"""

        for k, secondary in self._map.items():
            for v in secondary:
                yield (k,v)

    def add(self, k, v):
        """Add a pair (k,v) to multimap"""
        container = self._map.setdefault(k, []) #create empty list if needed 
        container.append(v)
        self._n +=1 
    
    def pop(self, k):
        secondary = self._map[k] #secondary map at position key k as a value
        v = secondary.pop() #pop that secondary container 
        if len(secondary) == 0: #if length of secondary container is 0
            del self._map[k] #then delete map at position k if no pairs left 
        
        self._n -=1 

        return (k,v) # example (1, [A,B,C,D]) 

    def find(self, k):
        """Return arbitrary (k,v) pair with given key (or raise Key Error)"""
        secondary= self._map[k] #may raise Key Error

        return (k,secondary[0])
    
    def find_all(self, k):
        """Generate ietartion of all K,v pair with given key"""
        secondary = self._map.get(k, []) #empty list by default
        for v in secondary:
            yield (k,v)


multimap = MultiMap()
multimap.add(2, ['A','B','C'])
multimap.add(1, ['C','D','E'])
multimap.add(1, ['H','I','J'])
print(multimap.find(2))


print(multimap.pop(2))

#returns only first value (occurrence) of key k 
for v in multimap.find(1):
    print(v)

#return all value associated with key k 
for v in multimap.find_all(1):
    print(v)

