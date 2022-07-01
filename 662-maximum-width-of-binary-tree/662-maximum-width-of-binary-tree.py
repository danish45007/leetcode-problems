# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = deque([1])
        max_width = 1
        while queue:
            # for each level calculate the width
            max_width = max(max_width,max(level)-min(level)+1)
            for _ in range(len(queue)):
                node = queue.popleft()
                node_serial_number = level.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(2*node_serial_number)
                if node.right:
                    queue.append(node.right)
                    level.append(2*node_serial_number+1)
        return max_width