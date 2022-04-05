# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
             return None
        
        if root1:
            val1 = root1.val
        else:
            val1 = 0
            
        if root2:
            val2 = root2.val
        else:
            val2 = 0
            
        # create new root node
        new_root = TreeNode(val1+val2)
        new_root.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None)
        new_root.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)
        
        return new_root
        