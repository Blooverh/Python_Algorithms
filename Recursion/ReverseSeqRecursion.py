# time complexity is O(n)
def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop-1:
        S[start] , S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

    return S

list=[9,8,7,6,5,4,3,2,1,0]
print(reverse(list, 0 , len(list)))