# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,_sum):
            if not node:
                return 0
            _sum = _sum*10 + node.val
            if not node.left and not node.right:
                return _sum
            return dfs(node.left,_sum) + dfs(node.right,_sum)
        return dfs(root,0)
            