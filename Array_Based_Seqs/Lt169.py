from collections import Counter, UserList
"""EXTREMELY SLOW SOLUTION USING JUST AN EXTRA ARRAY AS MEMORY"""
# def majorityElement(nums: UserList[int]) -> int:
#     counter=[ i * 0 for i in range(10000)] #list that will keep count of occurrences
#     print(counter)
#     if len(nums) <1:
#         return 0
    
#     for num in nums:
#         counter[num]+=1
    
#     return counter.index(max(counter))

# list=[6,5,5]

# print(majorityElement(list))

"""Faster Solution """
def majorityElement(nums: UserList[int]) -> int:
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol

# FASTEST SOLUTION
class Solution:
    def majorityElement(self, nums: UserList[int]) -> int:
        n = len(nums)
        dic = Counter(nums)
        for key, value in dic.items():
            if value > n/2:
                return key