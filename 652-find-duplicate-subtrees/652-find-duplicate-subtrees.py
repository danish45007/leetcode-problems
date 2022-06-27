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
            left_path = dfs(node.left,path)
            right_path = dfs(node.right,path)
            path += ','.join([str(node.val),left_path,right_path])
            if path in tree_map:
                tree_map[path] += 1
                if tree_map[path] == 2:
                    res.append(node)
            else:
                tree_map[path] = 1
            return path
        dfs(root,'')
        print(tree_map)
        return res