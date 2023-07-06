import PositionalList

class FavoritesList(PositionalList):
    """List of elements ordered from most frequently accessed to 
    least frequently accessed."""

    #Item class
    class _Item:
        __slots__='_value','_count' #streamline memory usage
        def __init__(self, e):
            self._value=e #the user's element
            self._count=0 #access count initially 0

    #Non Public utilities
    def _find_position(self, e):
        """Search for element e and return its position or None if not found"""
        walk= self._data.first()
        while walk is not None and walk.element()._value !=e:
            walk=self._data.after(walk)
        
        return walk
    
    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count"""
        if p != self._data.first(): #consider moving
            cnt=p.element().count
            walk=self._data.before(p)
            if cnt > walk.element()._count: #must shift forward
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk= self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) #delete/reinsert
    
    #public methods
    def __init__(self):
        """create an empty favorites list"""
        self._data = PositionalList() # will be list of _Item instances

    def __len__(self):
        """Return the number of entries of favorites list"""
        return len(self._data)
    
    def is_empty(self):
        """Return true if favorites list is empty"""

        return len(self._data) == 0
    
    def access(self, e):
        """Access element e, thereby increasing its access count"""
        p=self._find_position(e)
        if p is None:
            p =  self._data.add_last(self._Item(e)) # if element e not in fav list add to the last position of favorites list
        p.element()._count+=1 # increment the count of the element e whether it already exists or was just added
        self._move_up(p) # "insertion sort" to move element in the list 
    
    def remove(self, e):
        """Remove element from the favorites list"""
        p = self._find_position(p)

        if p is not None: 
            self._data.delete(p) #delete element at position p

    def top(self, k):
        """generate a sequence that shows the first K entries of the favorite list in terms of access count"""
        if not 1<= k <= len(self):
            raise ValueError('Illegal value for k')
        
        walk= self._data.first()
        for j in range(k):
            item=walk.element() # element of list is _Item
            yield item._value # report user's element
            walk=self._data.after(walk)