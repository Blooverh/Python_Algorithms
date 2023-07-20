
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create empty list of length of the nums list that will read list from left to right
        leftProd = [0] * len(nums)

        ## create empty list of length of the nums list that will read list from right to left
        rightProd= [0] * len(nums)

        leftProd[0] =1 #since nums[0] has nothing at the left of it we put 1
        rightProd[len(nums) - 1]= 1 #since nums[-1] has nothing to the right of it we put 1

        for i in range (1, len(nums)):
            leftProd[i] = leftProd[i-1] * nums 

            rightProd[len(nums)- i -1] = rightProd[len(nums)-i] * nums[len(nums)-i] #multiplies every element to the right of i

        ans = [] #empty list that will contain the product

        for i in range(len(nums)): 
            ans.append(leftProd[i] * rightProd[i]) #multiply noth arrays at the same index

        return ans
            