# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        min_depth = float('inf')
        def dfs(curr_node,curr_depth):
            nonlocal min_depth
            if not curr_node:
                return 0
            if not curr_node.left and not curr_node.right:
                min_depth = min(min_depth,curr_depth+1)
            if curr_node.left:
                dfs(curr_node.left,curr_depth+1)
            if curr_node.right:
                dfs(curr_node.right,curr_depth+1)
        
        dfs(root,0)
        return min_depth if min_depth != float('inf') else 0
        
        
        
        # bfs