# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        going_right = True
        while queue:
            level_res = []
            queue_len = len(queue)
            for _ in range(queue_len):
                if going_right:
                    top = queue.popleft()
                    level_res.append(top.val)
                    if top.left:
                        queue.append(top.left)
                    
                    if top.right:
                        queue.append(top.right)
                else:
                    top = queue.pop()
                    level_res.append(top.val)
                    if top.right:
                        queue.appendleft(top.right)
                    if top.left:
                        queue.appendleft(top.left)
            res.append(level_res)
            going_right = not going_right
        return res
                    