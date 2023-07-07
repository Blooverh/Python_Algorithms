"""Move to front heuristic of favorites List ADT"""
import FavoritesList
import PositionalList
class FavoritesListMTF(FavoritesList):
    """list of elements ordered with Move to front heuristic"""

    #override _move_up to provide move to front semantics
    def _move_up(self, p):
        """Move accessed item at position p to front of the list"""

        if p != self._data.first():
            self._data.add_first(self._data.delete(p)) #the item at p will be deleted but added to front of the list 

    #override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k element in terms of access count"""

        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        
        #begin making a copy of original list
        temp= PositionalList()
        for item in self._data: #positional lists support iteration
            temp.add_last(item)

        #repeatedly find, report and remove element with largest count
        for j in range(k):
            #find and report next highest from temp
            highPos = temp.first()
            walk=temp.after(highPos)

            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                
                walk= temp.after(walk)
            #found the element with the highest count
            yield highPos.element._value #report element to user
            temp.delete(highPos) #remove element from the temp list to get next largest element count