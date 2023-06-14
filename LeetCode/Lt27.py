from collections import UserList


class Solution:
    def removeElement(self, nums: UserList[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i