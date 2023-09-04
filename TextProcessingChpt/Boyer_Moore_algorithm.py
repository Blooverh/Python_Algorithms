
def find_boyer_moore(T, P):
    """Return the lower index of T at which substring P begins else -1"""

    n= len(T)
    m= len(P)

    if m==0: return 0 # a base case 
    
    last = {} # build last dictionary

    for k in range(m):
        last[P[k]] = k #later occurrences overwrites

    # align end of pattern at index m-1 of text
    i = m-1 # an index into T
    k = m-1 # an index into P

    while i < n:
        if T[i] == P[k]: #matching character
            if k == 0: 
                return i # pattern begins at index i of T
            else:
                i-=1 #examine previous character
                k-=1 # of both T and P
        else:
            j = last.get(T[i], -1) # last(T[i]) is -1 if not found
            i += m - min(k, j + 1) # case analysis for jump step
            k = m - 1 # restart at the end of the pattern for P

    return -1