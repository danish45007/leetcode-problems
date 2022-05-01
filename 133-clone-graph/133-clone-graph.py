"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        def clone(node):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for n in node.neighbors:
                new_neighbors = clone(n)
                copy.neighbors.append(new_neighbors)
            return copy
        return clone(node)