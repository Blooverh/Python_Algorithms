def isPalindrome( s: str) -> bool:
    punctuation_marks = [chr(32),chr(33), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39),
                     chr(40), chr(41), chr(42), chr(43), chr(44), chr(45), chr(46),
                     chr(47), chr(58), chr(59), chr(60), chr(61), chr(62), chr(63),
                     chr(64), chr(91), chr(92), chr(93), chr(94), chr(95), chr(96),
                     chr(123), chr(124), chr(125), chr(126)]
    
    # replace any punctiation or space into nothing
    for point in punctuation_marks:
        if point in s:
            s= s.replace(point, "")
    """s=re.sub('[^a-z0-9]', '', s) this can be used to decrease file memory
    by looking for a pattern based on regular expression module (re)
    and removing all characters that are not a-z and 0-9 and subbing them with ''
    """
    #make string all lowercase        
    s=s.lower()
    
    #base case if string is empty
    if len(s) == 0:
        return True

    return s == s[::-1] #return true if string s is equal to reverse of s string



print(isPalindrome("A man, a plan, a canal: Panama"))
