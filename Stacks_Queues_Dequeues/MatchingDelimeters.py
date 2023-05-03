"""This algorithm checks whether delimeters ([{}]) are paired correctly using stacks"""

from StackClass import Stack
def is_matched(expr):
    """Return True if all delimeters are properly matched, False other wise"""

    lefty='({['
    righty=')}]'
    stack= Stack()

    for c in expr:
        if c in lefty:
            stack.push(c) #Pushing left delimeter
        elif c in righty:
            if stack.isEmpty(): #if the stack is empty a mismatch of delimeter happened and returns false
                return False
            if righty.index(c) != lefty.index(stack.pop()): #if indices of righty and lefty elements do not match return false
                return False
    
    return stack.isEmpty()

expression='({[]})'
print(is_matched(expression))
print(is_matched("(}(][]))"))   