# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_max = root.val
        res = 0
        def dfs(node,max_val):
            nonlocal res
            if not node:
                return 0
            if max_val > node.val:
                res = 0
            else:
                res = 1
            max_val = max(max_val,node.val)
            res += dfs(node.left,max_val)
            res += dfs(node.right,max_val)
            return res
        dfs(root,curr_max)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        curr_max = root.val
        def dfs_pre_order(node,max_val):
            if not node:
                return 0
            if(max_val <= node.val):
                res = 1
            else:
                res = 0
            max_val = max(max_val,node.val)
            res += dfs_pre_order(node.left,max_val)
            res += dfs_pre_order(node.right,max_val)
            return res        
        return dfs_pre_order(root,curr_max)
            