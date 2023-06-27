"""Function for the sum of 2 lists with the same size and multiplication  """
def sum(list1, list2):
    """create a total list filled with 0 from length of each row """
    total= [ [0] * len(list1[0]) for _ in range(len(list1))]

    if len(list1) == len(list2) and len(list1[0]) == len(list2[0]):
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                total[i][j] = list1[i][j] + list2[i][j]
    else:
        raise ValueError('both lists have different dimensions')        
    
    for row in total:
        print(row)

#O(n^3)
def mult(list1, list2):
    total=[[0] * len(list1) for _ in range(len(list2[0]))]
    if len(list1) == len(list2[0]) and len(list1[0]) == len(list2):
        for i in range(len(list1)):
            for j in range(len(list2[0])):
                for k in range(len(list1[0])):
                    total[i][j] += list1[i][k] * list2[k][j] 
    else:
        raise ValueError('Lists do not follow dot product rules')

    for row in total:
        print(row)
    return

list1=[[9,3], 
       [2,1], 
       [1,6]]

list2=[[2,5],
        [4,1],
        [4,3]]

list3=[[1,2,3],
       [4,5,6]]

list4= [[7,8],
        [9,10],
        [11,12]]

print(sum(list1, list2))
print()
print(mult(list3, list4))
