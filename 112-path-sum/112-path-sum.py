# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs_pre_order(node,curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right:
                return curr_sum == targetSum
            return (dfs_pre_order(node.left,curr_sum) or dfs_pre_order(node.right,curr_sum))
        return dfs_pre_order(root,0)
            