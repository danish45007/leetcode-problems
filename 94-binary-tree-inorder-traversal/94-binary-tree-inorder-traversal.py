# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs_inorder(node):
            if not node:
                return 
            dfs_inorder(node.left)
            res.append(node.val)
            dfs_inorder(node.right)
        dfs_inorder(root)
        return res