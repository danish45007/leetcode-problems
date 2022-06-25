"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepCopyMap = {None: None}
        current = head
        while current:
            copyNode = Node(current.val)
            deepCopyMap[current] = copyNode
            current = current.next
        current = head
        while current:
            copyNode = deepCopyMap[current]
            copyNode.next = deepCopyMap[current.next]
            copyNode.random = deepCopyMap[current.random]
            current = current.next
        
        return deepCopyMap[head]

        