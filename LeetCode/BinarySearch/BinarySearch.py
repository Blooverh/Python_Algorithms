
"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity."""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        high= len(nums) - 1 

        if len(nums) <= 1 and nums[0] == target:
            return 0

        while low  <= high:
            mid = (low+high)//2

            if target < nums[mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                low = mid + 1

        return -1
    

sol= Solution()
array=[5]
target=-5
print(sol.search(array, target))