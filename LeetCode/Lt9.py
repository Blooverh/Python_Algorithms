def isPalindrome(x: int) -> bool:
    if x < 0: 
        return False
    
    if str(x) == str(x)[::-1]:
        return True
    
    return False

print(isPalindrome(121))