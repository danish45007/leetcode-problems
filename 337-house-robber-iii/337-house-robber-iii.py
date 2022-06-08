# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # returns: [max_with_root,max_without_root]
        def dfs(root):
            if not root:
                return [0,0]
            left_tree = dfs(root.left)
            right_tree = dfs(root.right)
            max_with_root = root.val + left_tree[1] + right_tree[1]
            max_without_root = max(left_tree) + max(right_tree)
            return [max_with_root,max_without_root]
        
        return max(dfs(root))