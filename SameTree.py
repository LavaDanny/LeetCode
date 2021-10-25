# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getVals(self, root, valArr):
        
        if(root == None):
            valArr.append('null')
            return valArr
        else:
            valArr.append(root.val)
            valArr = self.getVals(root.left, valArr)
            valArr = self.getVals(root.right, valArr)
        
        return valArr
            
        
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pVals = self.getVals(p, [])
        qVals = self.getVals(q, [])
        
        if(pVals == qVals):
            return True
        else:
            return False