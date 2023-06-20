# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """We iterate through list with current, pointing current to 
        next next current node if next node to current is equal to current
         after pointing nodes to correct positions we return head of each node """
        current = head 
        while current:
            while current.next  and current.next.val == current.val:
                current.next = current.next.next
            
            current = current.next

        return head 
