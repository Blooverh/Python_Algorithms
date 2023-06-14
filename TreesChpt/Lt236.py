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

        l = self.lowestCommonAncestor(root.left, p, q) #recursion to left child of each subroot
        r = self.lowestCommonAncestor(root.right, p, q) #recursion to rigth child of each subroot

        # if subroot of l is p and subroot of r is q then return current root of the recursion
        if l and r: 
            return root
        
        # case for if a tree node is descendent of itself
        return l or r