"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
from collections import UserList
class Solution:
    def containsDuplicate(self, nums: UserList[int]) -> bool:
        """Create a new set and append objects from list nums to the new set 
        if the new set has less elements than list nums, then 
        there is repeated numbers returning true"""

        copyList= set() #creates empty set 
        
        # base case 
        if len(nums) <= 1:
            return False
        
        #main case 
        for num in nums:
            copyList.add(num)
        
        if len(copyList) < len(nums):
            return True
        
        return False
    
test= Solution()
list=[1,2,3,4]

print(test.containsDuplicate(list))