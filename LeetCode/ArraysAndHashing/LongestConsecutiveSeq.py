from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        sort array
        variable counter to keep count of consecutive elements 
        once nums[i+1] - nums[i] > 1 
        append current counter to a list 
        and reset count and continue the pass
        until list is done
        append the current counter 

        return the max element in the list that contains the counters
        """

        #base cases
        if len(nums) <= 1:
            return len(nums)

        sortedNums = sorted(nums)
        print(sortedNums)
        counter=1
        counters=[]
        for i in range(1 , len(sortedNums)):
            if sortedNums[i] - sortedNums[i-1] == 1:
                counter +=1
            elif sortedNums[i] - sortedNums[i-1] <= 0:
                counter = counter
            elif sortedNums[i] - sortedNums[i-1] > 1:
                counters.append(counter)
                counter=1

        
        counters.append(counter)
        print(counters)
        return max(counters)

a =Solution()
arr= [9,1,4,7,3,-1,0,5,8,-1,6]
print(a.longestConsecutive(arr))