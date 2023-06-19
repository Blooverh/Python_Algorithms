"""Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order."""

"""THIS IS A TYPICAL BINARY SEARCH PROBLEM"""
from collections import UserList
class Solution:
    def searchInsert(self, nums: UserList[int], target: int) -> int:

        if len(nums) ==0:
            return 0

        low= 0
        high= len(nums)

        while low < high:
            mid=(low + high) //2

            if nums[mid] > target:
                high =  mid
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid +1 
        """In case element not in list with the srkink of the list, last element for search will be lowest
        position the element could have been if it was in the list """
        return low 