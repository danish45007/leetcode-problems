'''
Description
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example1

Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Example2

Input: {3,9,8,4,0,1,7}
Output: [[4],[9],[3,0,1],[8],[7]]
Explanation:
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

'''

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

from collections import defaultdict
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        column_map = defaultdict(list) #{x: node}
        min_col = float('inf')
        max_col = float('-inf')
        queue = deque()
        queue.append((0,root)) #x,TreeNode

        while queue:
            x,node = queue.popleft()
            column_map[x].append(node.val)
            min_col = min(min_col,x)
            max_col = max(max_col,x)

            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x+1,node.right))
        res = []
        for col in range(min_col,max_col+1):
            res.append(column_map[col])
        return res


