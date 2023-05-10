from queue import Empty


class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage"""

    class _Node:
        """Lightweight, non public class for storing a singly linked node"""
        __slots__= '_element', '_next' #streamline memory usage

        def __init__(self, element, next): #initialize node fields 
            self._element=element # reference to user's element
            self._next=next #reference to the next node 
        

    def __init__(self):
        """create empty stack"""
        self._head=None #with stack empty head points to NULL 
        self._size=0 #Because stack is empty size is 0

    def __len__(self):
        """Retrun the number of elements in the stack"""
        return self._size
    
    def isEmpty(self):
        """Boolean return for true is size = 0 false otherwise"""
        return self._size==0
    
    def push(self, e):
        """Add element at the head/ top of the stack"""
        self._head=self._Node(e, self._head) #create and link new node, node takes element e argument
        self._size+=1 #increase size of the stack when node is inserted in the list

    def top(self):
        if self._isEmpty():
            raise Empty('stack is empty')
        return self._head._element #shows which element is at the top of the singly linked list
    
    def pop(self):
        """Remove and return node on top of the stack, Rause empty exception if the stack is empty"""
        if self.isEmpty():
            raise Empty('Stack is empty')
        
        answer= self._head._element #answer holds reference to head element
        self._head=self._head._next #head now becomes the next node to previous head
        self._size-=1 #decrease the size of the stack

        return answer #return the element that was held by answer
    