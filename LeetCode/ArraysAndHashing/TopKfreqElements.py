

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        sorted_vals= sorted(freq.values(), reverse= True)
        sorted_dict={}

        for i in sorted_vals:
            for k in freq.keys():
                if freq[k] == i:
                    sorted_dict[k] = freq[k]

        ans= [] 
        for key in sorted_dict.keys():
            if len(ans) < k-1:
                ans.append(key)
        return ans
            


sol= Solution()
list= [3,0,1,0]
k=1

print(sol.topKFrequent(list, k))