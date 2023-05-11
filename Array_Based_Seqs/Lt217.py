"""Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct."""
from collections import UserList

"""Possible ways to do it: 
1. create a set that will hold the copy of the numbers in the original element
when a number in the original array already exists in the copy set return true else return false  

We Use a set because SETS CANNOT CONTAIN DUPLICATE ELEMENTS AND USE HASHING TO PERFORM THE LOOKUPS
RATHER THAN PERFORMING LINEAR LOOKUP, SO CHANCES OF FINDING DUPLICATES FASTER IS HIGHER

NOTE: if we sort the list we increase the chance of faster look up rather than the set because the set 
takes more memory due to space complexity
"""

class Solution:
    def containsDuplicate(self, nums: UserList[int]) -> bool:
        copy=set()

        if len(nums) < 2:
            return False
        
        for i in range(len(nums)):
            if nums[i] not in copy:
                copy.add(nums[i])
            else:
                return True
            
        return False
            
Solution1= Solution() 

list1=[1,2,3,1]

answer=Solution1.containsDuplicate(list1)
print(answer)