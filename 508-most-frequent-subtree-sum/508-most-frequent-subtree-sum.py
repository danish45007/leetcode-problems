# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        tree_sum = {}
        max_freq_count = 0
        def dfs(node):
            nonlocal max_freq_count
            if not node:
                return 0
            # post order left, right, root
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_sum = left_sum + node.val + right_sum
            tree_sum[curr_sum] = 1 + tree_sum.get(curr_sum,0)
            max_freq_count = max(max_freq_count,tree_sum[curr_sum])
            return curr_sum
        dfs(root)
        res = []
        for key,val in tree_sum.items():
            if val == max_freq_count:
                res.append(key)
        return res
                
            