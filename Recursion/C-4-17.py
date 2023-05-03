def isPalindrome(str):

    if len(str) <2:
        return True

    if str[0] != str[-1]:
        return False
    print(str)
    """Every time the function is called the array decrements in size and the 
    first and last elements are ignored, thus traveling through the array
    Thus with recursion the size of the array decreases """
    return isPalindrome(str[1:-1])
    
print(isPalindrome('racecar'))
print(isPalindrome('hello'))