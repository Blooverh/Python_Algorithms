

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left= None, right = None):
        self.val= val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case if subtree is empty

        if root is None:
            return 0
        
        # depth of subtrees
        leftDepth =  self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        # if both subtrees are empty

        if root.left is None and root.right is None:
            return 1
        
        # if left subtree is empty return depth of right subtree after adding 1 to it (root)
        if root.left is None and root.right is not None:
            return rightDepth + 1 
        
        #if right subtree is empty return depth of left subtree after adding 1 to it (root)
        if root.left is not None and root.right is None:
            return leftDepth + 1
        
        return min(leftDepth , rightDepth) + 1 