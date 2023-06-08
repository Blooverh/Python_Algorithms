

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Implement depth
	    def depth(node: Optional[TreeNode]) -> int:
		    return 1 + max(depth(node.left), depth(node.right)) if node else 0

	    return depth(root.left) + depth(root.right)  # calculate diameter