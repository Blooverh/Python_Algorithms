import SortedTableMap

class CostPerformanceDatabase:
    """Maintain a database of maximal (cost, performance) pairs"""

    def __init__(self):
        """create an empty database """
        self._M = SortedTableMap() # or more efficient map

    def best(self, c):
        """return (cost,performance) pair with largest cost not exciding c
        
        return None if there is no such pair"""

        return self._M.find_le(c) # SortedMap utility for less or equal comparison

    def add(self, c, p):
        """Add new entry with cost c and performance p"""

        #determine if (c,p) is dominated by any pair existent 
        other = self._M.find_le(c) # other is at least as cheap as c, other is an existing pair in map
        
        if other is not None and other[1] >= p: #if its perfomance is as good
            return # (c,p) is dominated, so ignore and do not add pair as it is a maxima
        
        self._M[c] = p #else add (c,p) to database

        #now remove any pairs that are dominated by (c,p) if (c,p) is a Maxima pair 
        other =  self._M.find_gt(c) # other more expensive than c, existing pair in map
        
        while other is not None and other[1] <=p:
            del self._M[other[0]] # delete existing pairs that are dominated by the "adding pair"
            other= self._M.find_gt(c) # continue comparison to next pair as previous was deleted
