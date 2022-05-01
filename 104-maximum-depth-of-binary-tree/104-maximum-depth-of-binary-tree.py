# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        q = deque()
        # add the root node
        level = 0
        q.append(root)
        while q:
            # iterate over all the elements in the current level
            for i in range(len(q)):
                node  = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        return level
        