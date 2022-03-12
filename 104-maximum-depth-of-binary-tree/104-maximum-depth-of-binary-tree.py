# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base condition
        if not root:
            return 0
        # hypothesis
        left_node_height = self.maxDepth(root.left)
        right_node_height = self.maxDepth(root.right)
        # induction
        return 1 + max(left_node_height,right_node_height)
        
        