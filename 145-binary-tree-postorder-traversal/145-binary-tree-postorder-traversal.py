# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack =[]
        cur = root
        
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res[::-1]
            
            
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
            