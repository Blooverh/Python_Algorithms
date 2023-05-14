from queue import Empty


class LinkedQueue:
    """FIFO queue implementation using linked lists"""
    #creating the node object that will hold the element value and the pointer to next element
    class _Node:
        __slots__='_element', '_next' #for streamline memory usage

        #constructor
        def __init__(self, element, next):
            self._element=element #reference to element 
            self._next=next #reference pointer to the next node 

    def __init__(self):
        #creating an empty queue
        self._head=None #with empty queue head has to have Null value 
        self._tail= None  #same for tail 
        self._size=0 #queue is empty so size is 0

    def __len__(self):
        return self._size # returns the number of elements existing in the queue 
    
    def _isEmpty(self):
        return self._size==0 #returns boolean value for whether queue is empty (size 0) or not 
    
    def first(self):
        if self._isEmpty():
            raise Empty('Queue is empty')
        return self._head._element #returns the value of the head element
    
    def dequeue(self):
        """Remove and return the first element of the Queue due to FIFO
        Raise empty exception is queue is empty"""

        if self._isEmpty():
            raise Empty('queue is empty')
        
        answer = self._head._element #answer is the head element that will be dequeued from the queue
        self._head=self._head._next # assign head node to next element pointer 
        self._size-=1

        #if queue only has 1 element and we dequeue, queue becomes empty 
        #so we have to set tail pointer to None
        if self._isEmpty():
            self._tail=None

        return answer
    
    def enqueue(self,e):
        """Add an element to back of the queue"""
        newest=self._node(e, None) #newest node will have element e and pointer to Null before we add it to queue

        """In case of whether the queue is empty or not where to put new node in queue"""
        if self._isEmpty():
            self._head= newest
        else:
            self._tail._next=newest

        self._tail=newest #update reference to tail node
        self._size+=1 #increase the size as queue increased in size 


