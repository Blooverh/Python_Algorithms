"""Lowest Common Ancestor of a Binary Tree
iven a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q: #if root is none or is equal to p or q return the root
            return root

        l = self.lowestCommonAncestor(root.left, p, q) 
        r = self.lowestCommonAncestor(root.right, p, q)

        # check if both recursion return the node if p or q is equal to that node
        # if for both subtrees it returns the nodes then we return the root, because the recursion call value is the same
        # if p and q are in different subtrees 
        if l and r:
            return root
        
        #else return the node that its descendent of itself 
        return l or r