"""Recursive algorithm to find the product of 2 integers m and n using only addition and subtraction"""
def productRecursion(n, m):
    total=0
    if m ==0 or n==0:
        return 0
    elif m >0 and n>0 :
        for _ in range(m):
            total+=n
    elif (m >0 and n<0):
        if n%2==0:
            for _ in range(m):
                total+=abs(n)
        else:
            total+=n
    elif n>0 and m<0:
        if m%2==0:
            for _ in range(n):
                total+=m
        else:
            total+=m
    elif n<0 and m<0:
        for _ in range(abs(m)):
                total+=abs(n)
    return total

print(productRecursion(4,3)) #correct
print(productRecursion(3,0)) #correct
print(productRecursion(-4,-3))#correct
print(productRecursion(3,-4))
print(productRecursion(-2,2))#correct