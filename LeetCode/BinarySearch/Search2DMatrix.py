"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        checkList=matrix[0]

        for row in range(len(matrix)):
            if target <= matrix[row][-1]:
                checkList = matrix[row]
                break
        
        low =0
        high = len(checkList) -1

        while low <= high:
            mid = (high+low) // 2

            if target < checkList[mid]:
                high = mid - 1
            elif target == checkList[mid]:
                return True
            else:
                low = mid + 1

        return False




sol=Solution()

DArray=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target= 13
print(sol.searchMatrix(DArray, target))
