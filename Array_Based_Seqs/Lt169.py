from collections import UserList
"""EXTREMELY SLOW SOLUTION USING JUST AN EXTRA ARRAY AS MEMORY"""
def majorityElement(nums: UserList[int]) -> int:
    counter=[ i * 0 for i in range(10000)] #list that will keep count of occurrences
    print(counter)
    if len(nums) <1:
        return 0
    
    for num in nums:
        counter[num]+=1
    
    return counter.index(max(counter))

list=[6,5,5]

print(majorityElement(list))

    
