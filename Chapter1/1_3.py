"""This algorithm runs at O(n)"""
def minmax(data):
    min=data[0]

    for num in range(1,len(data)):
        if data[num] <= min:
            min=data[num]
    
    max= data[0]
    for num in range(1, len(data)):
        if data[num] >= max:
            max=data[num]
    
    return min, max

data=[2,3,1,6,5,8,4,9]
print(minmax(data))

