# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sum = []
        def dfs(node):
            if not node:
                return 0
            # post order manner (l->r->root)
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_node_sum = left_sum + right_sum + node.val
            tree_sum.append(curr_node_sum)
            return curr_node_sum
        total_sum = dfs(root)
        max_sum = 0
        for sub_tree1_sum in tree_sum:
            sub_tree2_sum = total_sum - sub_tree1_sum
            max_sum = max(max_sum,sub_tree1_sum*sub_tree2_sum)
        return max_sum % (10**9 + 7)