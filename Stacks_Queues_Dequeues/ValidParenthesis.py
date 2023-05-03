class Solution:
    def isValid(self, s: str) -> bool:
        dict={'(':')', '{':'}', '[':']'}
        stack=[] #Empty list that will take in this exercise the data struct stack

        for c in s:
            if c in dict:
                stack.append(c) # if element at c is in dictionary as a key push to stack
            elif len(stack) ==0 or dict[stack.pop()] !=c: #if the stack is empty or the value of the key (stack.pop) is not equal to element c return false
                return False
            
        return len(stack)==0 #check is length of stack is 0, if it is the Return true because all delimeters did match in the Str s