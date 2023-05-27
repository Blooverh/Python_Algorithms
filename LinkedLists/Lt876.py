"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""
from typing import Optional
class ListNode:

    def __init__(self, val=0, next=None):
        self.val=val
        self.next= next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast= head
        slow= head
        """We will move 2x fast node and 1x slow node"""

        while fast != None and fast.next != None:
            fast= fast.next.next
            slow= slow.next

        return slow