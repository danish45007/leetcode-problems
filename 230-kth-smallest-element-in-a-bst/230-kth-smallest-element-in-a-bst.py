# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        # inorder traversal
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            # reached end of left side
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            # add right for processing
            curr = curr.right
            