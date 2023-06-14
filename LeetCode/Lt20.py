class Solution:
    def isValid(self, s: str) -> bool:
        dict={'(':')', '{':'}', '[':']'} #dictionary to contain the pairs of k,v
        stack=[] #empty stack that will hold keys for future checking

        """
        :type s: str
        :rtype: bool
        """

        for c in s:
            if c in dict:
                stack.append(c) #append the key to stack
            # if length of stack is 0 or value of the element being popped from the dict is not character c return false 
            elif len(stack) == 0 or dict[stack.pop()] != c:  # 2
                return False

        return len(stack)==0 #check if length of stack is empty or full based on length