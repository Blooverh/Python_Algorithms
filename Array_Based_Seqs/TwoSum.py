from collections import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={} #Empty dictionary to hold index and value in a K,V manner 
        result=[]
        for i, j in enumerate(nums):
            result= target - j # result is subtraction of target - value J at index i 

            #If the result is in the dict return the value of the key result in the dict and the index i
            if result in dict:
                return [dict[result], i]
            
            dict[j]= i # element j will be key and index i will be value for the dict
