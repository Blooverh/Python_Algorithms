from queue import Empty


class Queue:
    """FIFO queue implementation using Python list"""

    DEFAULT_CAPACITY=10 #moderated capacity for all new Queues

    def __init__(self):
        """create an empty Queue"""
        self._data=[None] * Queue.DEFAULT_CAPACITY #Assign empty queue as a list of size DEFAULT CAPACITY of Null objects.
        self._size=0
        self._front=0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
    
    def isEmpty(self):
        """return True if size is == 0"""
        return self._size == 0
    
    def first(self):
        """Return but do not remove the object at the front of the queue
        Raise empty Queue exception if queue is empty"""

        if self.isEmpty():
            raise Empty('Queue is empty')
        
    def dequeue(self):
        """remove the object in front of the queue"""
        """Raise exception if Queue is empty"""

        if self.isEmpty():
            raise Empty('Queue is empty')
        
        answer= self._data[self._front] # removes the front object from the queue
        self._data[self._front] = None # assigns None at that position for garbage collection since we are moving rightward the queue as a circular list 
        self._front= (self._front+1) % len(self._data) #front object now becomes the next index based on modulus due to circular list 
        self._size -= 1 #decrease size of the Queue by 1 

        return answer
    
    def enqueue(self, e):
        """Add element to the back of the Queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data)) #Double size of the array to help with the object shifting when manipulating the Queue

        avail= (self._front + self._size) % len(self._data) #goes to the index  from remainder of the mod of (self._front + self._size) % 10 which is the back of the queue
        self._data[avail]=e #add element to back of the Queue
        self._size +=1 #increment size of the Queue once element is added at the back

    def resize(self, cap):
        """Resize to a new list of capacity >= len(self) """

        old=self._data #keep track of existing list by reference 
        self._data=[None] * cap #allocate list with new capacity 

        walk= self._front

        for k in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #intentionally shift
            walk= (1+walk) % len(old) #use old size as modulus
        
        self._front=0 #front has been realigned