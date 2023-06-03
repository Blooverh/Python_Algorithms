# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import UserList

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> UserList[UserList[int]]:

        if root is None:
            return root
        Q=[] # Queue for keeping nodes to visit

        returnList=[] # list that will keep subtree pairs aka siblings

        Q.append(root) # append 1st position which is root

        while len(Q) > 0:
            ans = [] #holds list of siblings 
            l= len(Q)

            for l in range(l):
                node= Q.pop(0)
                ans.append(node.val)
                 
                if node.left != None:
                    Q.append(node.left)

                if node.right != None:
                    Q.append(node.right)
            
            returnList.append(ans)
        return returnList
