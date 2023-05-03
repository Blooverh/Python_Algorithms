def countOccurrences(array, k):
    count=0

    for i in range(len(array)):
        if k == array[i]:
            count= count+1

    return count 

data=[2,3,4,5,2,4,2,4,1,2,4,5,7,8,2,7,9,10]

k=2
print(countOccurrences(data, k))
