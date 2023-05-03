"""This Script is the implementation of the stack class ADT using PYTHON LISTS"""

class Stack:
    """LIFO stack implementation using Python Lists as underlying storage"""

    #Constructor
    def __init__(self):
        """create empty stack"""
        self._data=[]

    def __len__(self):
        #returns the number of elements the stack holds 
        return len(self._data)
    
    def isEmpty(self):
        #True if empty stack false if not empty stack
        return len(self._data) == 0 
    
    def push(self, e):
        """Add element to the end of the list """
        self._data.append(e)

    def top(self):
        #Has to check whether the stack is empty or not
        #returns the last/top element in the stack as a reference but does not remove element from stack

        if self.isEmpty():
            raise IndexError('Stack is empty')
        else:
            return self._data[-1]
        
    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty')
        
        return self._data.pop()
    
    def print(self):

        if len(self._data) != 0:
            for i in range(len(self._data)):
                print(self._data[i])
        else:
            raise IndexError("Stack is empty")    
    
stack = Stack()

stack.push(3)
print(stack.isEmpty())
stack.print()
print(stack.top())
stack.pop()
print(stack.isEmpty())
stack.print()