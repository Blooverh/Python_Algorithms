"""This algorithm checks whether delimeters ([{}]) are paired correctly using stacks"""

from StackClass import Stack
def is_matched(expr):
    """Return True if all delimeters are properly matched, False other wise"""

    lefty='({['
    righty=')}]'
    stack= Stack()

    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.isEmpty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    
    return stack.isEmpty()

expression='({[]})'
print(is_matched(expression))
print(is_matched("(}(][]))"))   