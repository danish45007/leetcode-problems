# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum = 0
        def dfs(node):
            nonlocal curr_sum
            # reverse inorder right -> root -> left
            if not node:
                return 
            #apply dfs on right sub tree
            dfs(node.right)
            # right most left node
            temp_node_val = node.val
            node.val += curr_sum
            curr_sum += temp_node_val
            #on left sub tree
            dfs(node.left)
        dfs(root)
        return root
            