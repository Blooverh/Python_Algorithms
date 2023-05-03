def power(x,n):
    """Compute the value x**n for integer n without using power functio"""
    if n==0:
        return 1
    else:
        return x* power(x,n-1)
    
print(power(2,7))