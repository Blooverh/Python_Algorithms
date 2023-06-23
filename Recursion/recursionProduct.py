def product(m,n):

    if m ==1: #base case where if n * 1 return n 
        return n
    elif n == 1: #base case where if m * 1 return m 
        return m
    
    return m + product(m, n-1) # recursive call  

print(product(10,10))