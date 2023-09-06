

def find_KMP(T, P):
    """Return the lowest index of T at which substring P begins else -1"""

    n = len(T)
    m = len(P)

    if m == 0 :
        return 0
    
    fail = compute_kmp_fail(P) # utility method to precompute

    j=0
    k=0

    while j < n:
        if T[j] == P[k]:
            if k == m-1: # P[0: 1+k] matched thus far
                return j - m+1 # match is complete return first index where P starts in T
            
            j+=1
            k+=1
        elif k > 0: 
            k =  fail[k-1] # reuse suffix of P[0:k]
        else:
            j+=1
    
    return -1 #reached end without match

"""
a t c a m a l g a m a m a l g a m a t i o n
  a |m a l g a m a t i o n
    a |m a l g a m a t i o n
      a m a l g a m a|t i o n
                a m a|l g a m a t i o n
                    a m a l g a m a t i o n
"""

def compute_kmp_fail(P):
    """Utility that computes and returns KMP fail list"""

    m=  len(P)

    fail = [0] * m # by default presum overlap of 0 everywhere
    j=1
    k=0

    while j < m: # compute f(j) during this pass is nonzero
        if P[j] == P[k]: # k+1 character match thus far
            fail[j] = k+1
            j+=1
            k+=1
        elif k >0:
            k = fail[k-1] # k follows a matching prefix
        else: # no match foung starting at j
            j+=1

    return fail


"""
a m a l g a m a t i o n
0 1 2 3 4 5 6 7 8 9 10 11

    m    ==  a
    p[1] == p[0] - false j+=1 = j= 2 - fail -> [0,0,0,0,0,0,0,0,0,0,0,0]
    j=2 
    k=0

    a   ==  a
    p[2] == P[0] - true fail[2] = 1 - fail -> [0,0,1,0,0,0,0,0,0,0,0,0]
    j+=1 - j=3
    k+=1 = k=1

    l    ==   m
    p[3] == k[1] - false k = fail[k-1] - k = fail[1-1] - [0,0,1,0,0,0,0,0,0,0,0,0]
    j=3
    k=0

    .
    .
    .
    .

    fail = [0,0,1,0,0,1,2,3,0,0,0,0]


"""