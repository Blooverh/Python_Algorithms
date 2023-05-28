"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function."""

class MinStack:

    def __init__(self):
        self.A=[]
        self.B=[]

    def push(self, val: int) -> None:
        self.A.append(val)
        # if value is not in stack B already append to list if not 
        # checks min between value wanting to be pushed and top value of stack B
        #then push value if less than the number in stack B 
        self.B.append(val if not self.B else min(val, self.B[-1])) 
        
    def pop(self) -> None:
        self.A.pop()
        self.B.pop()

    def top(self) -> int:
        return self.A[-1] #returns top element of the stack

    def getMin(self) -> int:
        return self.B[-1] #returns the top element of stack B which holds the smallest value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()