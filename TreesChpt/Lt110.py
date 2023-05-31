"""Given a binary tree, determine if it is 
height-balanced (A height-balanced binary tree is a binary tree in 
which the depth of the two subtrees of every node never differs by more than one.)
""" 

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """ 
        if root == None:
            return True
        """Call helper method to calculate the height of each side and calculate it based on which node does have an 
        element"""
        l = self.depth(root.left)
        r = self.depth(root.right)
        """If absolute value of the subtraction of the depth of each side is less than 2 and both 
        nodes are not null return true, else if depth of onde side is bigger than the other by 2 
        units return false"""
        return (abs(l-r) <2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    """Calculates depth of each side based on which node is not null"""
    def depth(self,node):
        if node == None: return 0 # if node is none return 0 meaning there is no child node 
        return max(self.depth(node.left),self.depth(node.right))+1 # increment based on which node has children