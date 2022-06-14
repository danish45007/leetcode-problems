# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_dists = dfs(node.left)
            right_dists = dfs(node.right)
            
            for left_dist in left_dists:
                if left_dist >= distance:
                    continue
                
                for right_dist in right_dists:
                    res +=1 if left_dist + right_dist <= distance else 0
            
            return [dist+1 for dist in left_dists+right_dists]
        
        dfs(root)
        return res
                    