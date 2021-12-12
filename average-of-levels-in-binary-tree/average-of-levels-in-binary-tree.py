# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        q = deque()
        q.append(root)
        while len(q):
            level_sum = 0
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(float(level_sum)/level_size)
        
        return result
        