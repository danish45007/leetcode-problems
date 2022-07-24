# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = root.val
        def dfs(node):
            nonlocal max_path_sum
            if not node:
                return 0
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            left_val = max(left_node,0)
            right_val = max(right_node,0)
            max_path_sum_with_split = node.val + left_val + right_val
            max_path_sum = max(max_path_sum,max_path_sum_with_split)
            return node.val + max(left_val,right_val)
        dfs(root)
        return max_path_sum
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max path sum with split
        max_path_sum = root.val
        # this will return the path sum without split
        def dfs(node):
            nonlocal max_path_sum
            if not node:
                return 0
            left_path_sum = dfs(node.left)
            right_path_sum = dfs(node.right)
            # if left_path_sum is -ve don't consider the child into parent while calculating
            # parent path sum
            left_path_sum = max(left_path_sum,0)
            right_path_sum = max(right_path_sum,0)
            max_path_with_split = node.val + left_path_sum + right_path_sum
            # updating the result at each node split
            max_path_sum = max(max_path_sum,max_path_with_split)
            # return the max path sum without split which will used by the parent node
            return node.val + max(left_path_sum,right_path_sum)
        dfs(root)
        return max_path_sum
            
            
            