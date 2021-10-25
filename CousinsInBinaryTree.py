# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
    
class Solution(object):   
    
    #if val found, return depth and parent
    def findDepth(self, root, depth, target, parent):   
        
        if(root.val == target):
            return(depth, parent)
        
        else:
            if(root.left and root.right):
                return max(self.findDepth(root.left, depth + 1, target, root), self.findDepth(root.right, depth + 1, target, root))
            elif(root.left):
                return (self.findDepth(root.left, depth + 1, target, root))
            elif(root.right):
                return (self.findDepth(root.right, depth + 1, target, root))

            
            
    
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        #find nodes with val equal to x and y
        #check if they have different depths and different parents
        #return true or false
        
        node1depth, node1parent = self.findDepth(root, 0, x, root)
        node2depth, node2parent = self.findDepth(root, 0, y, root)
        
        if(node1depth == node2depth and node1parent != node2parent):
            return(True)
        else:
            return(False)
        
