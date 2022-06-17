# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if p == node or q == node:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            else:
                return l or r
        return dfs(root)