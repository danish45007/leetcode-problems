# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        swap = []
        stack = []
        prev = TreeNode(float('-inf'))
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            temp = stack.pop()
            if temp.val < prev.val:
                swap.append((prev,temp))
            
            prev = temp
            curr = temp.right
        swap[0][0].val,swap[-1][1].val = swap[-1][1].val,swap[0][0].val
                
             