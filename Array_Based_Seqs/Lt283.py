from collections import UserList
class Solution:
    def moveZeroes(self, nums: UserList[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 1:
            return nums

        l=0
        for r in range(len(nums)):
            #swap if right element is non-zero  and left element is 0
            if nums[r]!=0 and nums[l]==0:
               nums[l], nums[r] = nums[r], nums[l]
               
            # wait while we find a non-zero element to
            # left goes up one index if non 0 if it is 0, iterated through loop until r is non-zero again
            #so we can go up in the loop and swap again
            if nums[l] != 0:
                l += 1
        
        return nums

           

                

    

answer=Solution()
list=[0,1,0,3,12]
print(answer.moveZeroes(list))
