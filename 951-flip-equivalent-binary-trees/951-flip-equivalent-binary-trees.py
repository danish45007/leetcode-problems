# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 or not r2:
            return r1 == r2
        # if not r1 and not r2:
        #     return True
        if r1.val != r2.val: return False
        
        # checking the subtree
        # without flip
        res_without_flip = self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right,r2.right)
        return res_without_flip or self.flipEquiv(r1.left,r2.right) and self.flipEquiv(r1.right,r2.left)
        # return res_without_flip or res_with_flip
        