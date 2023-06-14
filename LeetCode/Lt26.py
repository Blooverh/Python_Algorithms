from collections import UserList


class Solution:
    def removeDuplicates(self, nums: UserList[int]) -> int:
        if len(nums) ==0:
            return 0
        k=1 #start from second position since first position is already correct and we start swapping from this index
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k]=nums[i+1] #if nums[i] != nums[i+1], append nums[i+1] at index k that starts at 1
                k+=1 #increment k to next index 
        
        return k