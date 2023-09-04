
def brute_force(T, P):
    """ return the lowest index of T at which substring P begins
    or else -1"""

    n= len(T)
    m = len(P)

    for i in range(n - m+1): #try every potential starting index within T
        k=0 #starting len for checking pattern P

        while k < m and T[i + k] == P[k]: # while kth character of P matches
            k+=1
        
        if k == m: #if ended of the pattern and k is equal to m then 
            return 1 # substring of T[i:i+m] matches P 
        
    return -1
       
