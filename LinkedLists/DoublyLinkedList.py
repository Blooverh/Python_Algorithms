class DoublyLinkedList:
    """Base class for providing a doubly linked list representation"""
    class _Node:
        __slots__='_element','_prev','_next'

        def __init__(self, element, prev, next):
            self.element=element
            self._prev=prev
            self._next=next
    
    def __init__(self):
        """create empty list with sentinel nodes"""
        self._header=self._Node(None,None,None) #created sentinel header node 
        self._trailer=self._Node(None, None, None) #created sentinal tail node
        self._header._next=self._trailer #pointer of sentinel header to tail sentinel
        self._trailer._prev=self._header # pointer of sentinel trailer back to header
        self._size=0 #size of the list itself is 0 even though we have sentinel nodes

    def __len__(self):
        return self._size #returns the number of elements in the list  


    def is_empty(self):
        return self._size==0 #returns boolean value on whether the list is empty or not 
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between 2 existing nodes  and return the new node inserted"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next= newest #links new pointer of predecessor to new node 
        successor._prev= newest #linked new pointer of successor backwards to new node

        self._size+=1 #increase the size of the list since new node was added 

        return newest #return new added node 
    
    def _delete_node(self, node):
        """Delete non sentinel node from the list and return its list """
        predecessor=node._prev #assign what is the predecessor node to the node passed in the argument
        successor= node._next #assign what is the successor node to the node passed in the argument to be deleted 
        predecessor._next= successor #link new successor to deleted node predecessor
        successor._prev= predecessor #link new predecessor to deleted node successor
        self._size-=1 #decrease size of list 

        element= node._element #record value of the element to be deleted 
        node._prev= node._next= node._element=None #link deleted node to itself for deprecation/deletion
        return element 
    

    