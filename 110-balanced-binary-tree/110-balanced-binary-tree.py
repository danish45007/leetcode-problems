# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True,0)
            left_tree = dfs(node.left)
            right_tree = dfs(node.right)
            node_height = 1 + max(left_tree[1],right_tree[1])
            if left_tree[0] and right_tree[0] and abs(left_tree[1]-right_tree[1]) <= 1:
                return (True,node_height)
            return (False,float('-inf'))
        
        return dfs(root)[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def dfs_post_order(root):
            if not root:
                return (0,True)
            
            left_height,left_balance = dfs_post_order(root.left)
            right_height,right_balance = dfs_post_order(root.right)
            balanced = left_balance and right_balance and abs(left_height-right_height) <= 1
            node_height = 1+max(left_height,right_height)
            return [node_height,balanced]
        return dfs_post_order(root)[1]
            