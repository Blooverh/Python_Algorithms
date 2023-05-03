def sumOfSquares(k):
    num=0
    sum=0
    list=[]
    while num < k:
        list.append(num)
        sum+=pow(num,2)
        num=num+1
        
    print(list)
    
    return sum

print(sumOfSquares(5))

def sum_of_sq(n):

    list_tot=[]
    for i in range(1,n):
        list_tot.append(i*i)
    
    print(list_tot)
    return sum(list_tot)

print(sum_of_sq(5))