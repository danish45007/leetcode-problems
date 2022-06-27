# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        tree_map = {}
        def dfs(node,path):
            if not node:
                return '#'
            path += ','.join([str(node.val),dfs(node.left,path),dfs(node.right,path)])
            if path in tree_map:
                tree_map[path] += 1
                if tree_map[path] == 2:
                    res.append(node)
            else:
                tree_map[path] = 1
            
            return path
        dfs(root,'')
        return res