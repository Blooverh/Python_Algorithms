"""Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise."""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow=head
        fast=head

        reversed_list=None
        
        #reverse left half of the list while searching the start point of the right half

        while fast != None and fast.next != None:

            temp= slow


            slow=slow.next
            fast=fast.next.next

            #place node at start of the reversed half
            temp.next= reversed_list
            reversed_list= temp

            """If there are an even number of elements in list
            do one more step to reach the 1st element of the secong list's half"""

        
        if fast != None:
            slow=slow.next
        
        #Compare reversed left half with the original right half
        while reversed_list != None and reversed_list.val == slow.val:
            reversed_list =reversed_list.next
            slow=slow.next

        return reversed_list == None
            
