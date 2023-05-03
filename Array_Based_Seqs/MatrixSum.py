"""Function for the sum of 2 lists with the same size"""
def sum(list1, list2):
    total=[[0] * len(list1) for j in range(len(list1[0]))]
    if len(list1) == len(list2) and len(list1[0]) == len(list2[0]):
        for i in range(len(list2)):
            for j in range(len(list2[0])):
                total[i][j]= list1[i][j]+list2[i][j]
    else:
        raise ValueError('The lists do not have the same size')

    return total

list1=[[1,1], [1,1], [1,1]]
list2=[[1,1], [1,1]]

print(sum(list1, list2))
