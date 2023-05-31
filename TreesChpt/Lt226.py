"""Given the root of a binary tree, invert the tree, and return its root."""

from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
            
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.right, root.left= root.left, root.right

        return root