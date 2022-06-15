# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def dfs(node):
            if node.left:
                graph[node.val].append((node.left.val,'L'))
                graph[node.left.val].append((node.val,'U'))
                dfs(node.left)
            if node.right:
                graph[node.val].append((node.right.val,'R'))
                graph[node.right.val].append((node.val,'U'))
                dfs(node.right)
        dfs(root)
        queue = deque([(startValue,'')])
        visited = set()
        visited.add(startValue)
        while queue:
            node,res = queue.popleft()
            if node == destValue:
                return res
            else:
                for edge,d in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge,res+d))
        return -1
                    