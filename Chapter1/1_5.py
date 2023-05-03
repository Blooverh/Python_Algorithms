def listOfsquares(k):
    list=[]

    for num in range(k):
        list.append(pow(num,2))
    
    print(list)
    print(sum(list))

listOfsquares(5)