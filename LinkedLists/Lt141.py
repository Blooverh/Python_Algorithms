"""Check if Linked List has a cycle"""
"""FLOYED CYCLES ALGORITHMS TURTLE AND RABIT ALGORITHM"""

#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast= head #create node that will run 2 nodes faster
        slow = head  #create node that will through each node

        while fast and fast.next: #while fast and fast.next are not NONE/NULL
            slow=slow.next # runs one by one
            fast= fast.next.next # jumps from 2 to 2 nodes 

            if fast == slow: #Once node slow and node fast refer to the same value return true
                return True

        return False