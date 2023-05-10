"""Merging 2 linked lists"""


from typing import Optional

class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode() #create head node with value 0 and a pointer to node none
        head_ptr= head #head pointer to link to head node
        

        while list1 and list2: #while node list1 and node list2 exists
            if list1.val < list2.val: #compare their node values 
                head.next = list1 #next node to head node is list1 node
                list1 = list1.next #moves to next node of current list1 node 
            else:
                head.next = list2 
                list2 = list2.next
            head = head.next #head becomes now the next node to current head node
        
        # In case one of the lists is bigger than the other attache rest of the nodes to merged linked list 
        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return head_ptr.next 