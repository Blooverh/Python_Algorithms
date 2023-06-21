

def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice fromS[start:stop]"""
    if start >= stop: # for empty array or if start literally has the same value as stop
        return 0
    elif start == stop-1: # in case array only has one element, or start and stop are differedn by one
        return S[start]
    else:
        mid = (start + stop) //2 #find mid point of current array being processed
        """Since it is a binary recursion, recursion decrements size of the array into 
        the smallest size then processes the sum between the numbers of the smallest iteration"""
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop) 
    
S = [1,2,3,4,5,6,7,8]

print(binary_sum(S, 0, 7))