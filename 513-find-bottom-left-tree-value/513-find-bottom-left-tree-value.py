# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def level_order_bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                curr_node = queue.popleft()
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)
            return curr_node.val
        return level_order_bfs(root)

        