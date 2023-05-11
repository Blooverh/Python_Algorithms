"""Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order."""
from collections import UserList
class Solution:
    def sortedSquares(self, nums: UserList[int]) -> UserList[int]:

        for idx in range(len(nums)):
            nums[idx]*=nums[idx]

        nums.sort()

        return nums