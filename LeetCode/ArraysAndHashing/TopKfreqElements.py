from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] =1
            else:
                freq[num] += 1

        #dictionary where items of dictionary are sorted in reverse, so key with heighest value is first
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)) #python built in method

        result = list(freq.keys())[:k] #list of the first k keys from the dictionary which contain keys with heighest values

        return result
            


sol= Solution()
l= [3,0,1,0]
k=1

print(sol.topKFrequent(l, k))