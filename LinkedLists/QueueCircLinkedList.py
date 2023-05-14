from queue import Empty


class CircularQueue:

    class _Node:
        __slots__= 'element', 'next'
        
         #constructor
        def __init__(self, element, next):
            self._element=element #reference to element 
            self._next=next #reference pointer to the next nodet

    #constructor
    def __init__(self):
        """create empty queue"""
        self._tail=None
        self._size=0

    def __len__(self):
        """return the number of elements in queue"""
        return self._size
    
    def isEmpty(self):
        return self._size==0
    
    def first(self):
        """return but not remove the element at front of the queue
        raise Empty exception if queue is empty"""

        if self.isEmpty():
            raise Empty('Queue is empty')
        
        head=self._tail._next #head is the node pointed from the tail pointer to create the cycle 

        return head._element
    
    def dequeue(self):
        
        if self.isEmpty():
            raise Empty('Queue is empty')
        
        #old head is the front element in queue that will be dequeued that is referenced from the tail pointer
        oldhead=self._tail._next 

        #if there is only one node that node cant have 2 references (head and tail)
        if self._size==1:
            self._tail=None 
        else:
            self._tail._next=oldhead._next

        return oldhead._element
    
    def enqueue(self, e):
        """Add element to back of the queue"""
        newest=self._Node(e, None) #create node pointing to null before adding to the queue 

        if self.isEmpty():
            newest._next=newest #points to itself as it is creating circular solution
        else:
            newest._next=self._tail._next #new node points to head 
            self._tail._next= newest #old tail points to new node 
        
        self._tail=newest #new node becomes the tail 
        self._size+=1 #increase size of queue as new node was added 

    
    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size >0:
            self._tail= self._tail._next #old head becomes the new tail
    
