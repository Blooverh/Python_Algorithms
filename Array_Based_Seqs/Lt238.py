from collections import UserList
class Solution:
    def productExceptSelf(self, nums: UserList[int]) -> UserList[int]:
        size = len(nums) 
        leftProduct = [0]*size #create empty list of length size that will run left to right 
        rightProduct = [0]*size #create empty list of length size that will run right to left
        leftProduct[0] = 1 #since array at 0 has nothing to the left we put 1
        rightProduct[size-1] = 1 #since array at size -1 has nothing to the right we put one
        
        for i in range(1,size):
            leftProduct[i] = leftProduct[i-1] * nums[i-1] #multiplies every element to the left of i 
            rightProduct[size-i-1] = rightProduct[size-i] * nums[size-i] #multiplies every element to the right of i
        
        ans = [] #empty list that will contain the product
        for i in range(size):
            ans.append(leftProduct[i] * rightProduct[i]) #multiply both arrays at same index 
        return ans
    
answer=Solution()
list=[1,2,3,4]
print(answer.productExceptSelf(list))