"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head # intialize current pointer as head 
        prev = None #initialize prev pointer as Null 

        while current: #loop till current points to null
            next= current.next #initialize next pointer as the next pointer of curr
            current.next = prev #assign prev pointer to curr's next pointer
            # assign current to prev and next to current
            prev = current 
            current = next

        return prev #return prev poiter to get reverse of the list


            
            
