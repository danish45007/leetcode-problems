# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_inorder_using_stack(node):
            stack = []
            res = []
            curr = node
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                if curr:
                    res.append(curr.val)
                    curr = curr.right
            return res
        return dfs_inorder_using_stack(root)
        
                