""" Implementation of a cyclic shift hash code computation 
for a character string using bit shift operations"""

def hash_code(s): 
    mask= (1 << 32) - 1 #limit to 32-bit integers 
    h=0

    for char in s:
        h = (h << 5 & mask) | (h >> 27) # 5 bit cyclic shift of running sum
        h += ord(char) #add in value of the next character

    return h