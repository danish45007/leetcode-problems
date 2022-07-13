# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            res = 1 + max(left_node,right_node)
            return res
        dfs(root)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        