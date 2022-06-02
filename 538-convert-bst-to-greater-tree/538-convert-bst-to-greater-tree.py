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
            if not node:
                return
            # opposite of in-order traversal R -> root -> left
            dfs(node.right)
            temp_node_val = node.val
            node.val += curr_sum
            curr_sum += temp_node_val
            dfs(node.left)
            return node
        return dfs(root)
            
            