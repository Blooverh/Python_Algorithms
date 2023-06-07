
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """if root is None return false because there is no tree"""
        if not root:
            return False
        
        """Use helper method to check if both nodes of each tree are equal"""
        if self.isSameTree(root, subRoot):
            return True

        """recursive call with new tree node as root and same subRoot until both trees are checked
        and have same values"""
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """if both exists check whether values are equal if not equal call original function to get new nodes
        if both values are equal check the other values on the rest of both trees"""
        if p and q: 
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return p is q