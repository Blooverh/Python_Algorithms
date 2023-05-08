from queue import Empty

class Dequeue:
    """Double ended queue can insert and delete at end and front of the queue"""

    DEFAULT_CAPACITY=10 #moderated capacity for all new QUEUES 

    def __init__(self):
        """create empty double ended queue"""
        self._data=[None] * Dequeue.DEFAULT_CAPACITY 
        self._size=0
        self._front=0

    def __len__(self):
        """Return number of elements in the Dequeue and not the default capacity"""
        return self._size
    
    def isEmpty(self):
        """Returns whether the Dequeue is empty or has elements"""
        return self._size ==0
    
    def first(self):
        """Return but not remove element at the front of the Dequeue
        if queue is not empty"""

        #if dequeue is empty raise exception error
        if self.isEmpty():
            raise Empty("Dequeue is empty")

        #returns element at front position
        return self._data[self._front]
    
    def last(self):
        """Return element at beggining of the Dequeue"""
        return self._data[(self._front + self._size - 1)%len(self._data)]
    
    def dequeue_front(self):
        """Remove object at the front of the Dequeue"""

        if self.isEmpty():
            raise Empty("Dequeue is empty")

        answer= self._data[self._front] # removes the front object from the queue
        self._data[self._front] = None # assigns None at that position for garbage collection since we are moving rightward the queue as a circular list 
        self._front= (self._front+1) % len(self._data) #front object now becomes the next index based on modulus due to circular list 
        self._size -= 1 #decrease size of the Queue by 1 

        return answer
    
    def dequeue_last(self):
        """Remove object at the back of the Dequeue"""

        if self.isEmpty():
            raise Empty("Dequeue is empty")
        
        back_element= self._data[self._size()]
        answer= self._data[back_element] # removes the bacl object from the dequeue
        self._data[back_element] = None # assigns None at that position for garbage collection since we are moving rightward the queue as a circular list 
        back_element= (self._front + self._size - 1) % len(self._data) #back object now becomes the next index based on modulus due to circular list 
        self._size -= 1 #decrease size of the DeQueue by 1 

        return answer
    
    def enqueue_back(self, e):
        """Add element to the back of the Queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data)) #Double size of the array to help with the object shifting when manipulating the Queue

        avail= (self._front + self._size) % len(self._data) #goes to the index  from remainder of the mod of (self._front + self._size) % 10 which is the back of the queue
        self._data[avail]=e #add element to back of the Queue
        self._size +=1 #increment size of the Queue once element is added at the back

    def enqueue_front(self,e):
        if self._size == self.DEFAULT_CAPACITY:
            self._dequeue_last()

        self._front = (self._front-1) % len(self._data)
        self._data[self._front]=e
        self._size+=1
    

    def resize(self, cap):
        """Resize to a new list of capacity >= len(self) """

        old=self._data #keep track of existing list by reference 
        self._data=[None] * cap #allocate list with new capacity 

        walk= self._front

        for k in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #intentionally shift
            walk= (1+walk) % len(old) #use old size as modulus
        
        self._front=0 #front has been realigned
