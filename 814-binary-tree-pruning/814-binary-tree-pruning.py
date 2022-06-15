# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        # return True if from there is 1 in path
        # else returns False
        def dfs(node):
            if not node:
                return False
            
            if not node.left and not node.right:
                return node.val == 1
            left_has_one = dfs(node.left)
            right_has_one = dfs(node.right)
            
            if left_has_one and right_has_one:
                return True
            elif left_has_one and not right_has_one:
                node.right = None
                return True
            elif not left_has_one and right_has_one:
                node.left = None
                return True
            else:
                if node.val == 1:
                    node.left = None
                    node.right = None
                    return True
                else:
                    return False
        
        return root if dfs(root) else None
    
        
        