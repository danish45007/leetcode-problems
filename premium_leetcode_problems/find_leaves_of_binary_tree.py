'''
Description
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.


Example
Example1
Input: {1,2,3,4,5}
Output: [[4, 5, 3], [2], [1]].
Explanation:

    1
   / \
  2   3
 / \     
4   5    
Example2
Input: {1,2,3,4}
Output: [[4, 3], [2], [1]].
Explanation:

    1
   / \
  2   3
 /
4 
'''


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import defaultdict

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        res = defaultdict(list)

        # write your code here
        def dfs(node,layer):
            if not node:
                return layer
            
            # post order
            left = dfs(node.left,layer)
            right = dfs(node.right,layer)
            layer = max(left,right)
            res[layer].append(node.val)
            return layer + 1
        dfs(root,0)
        result = []
        for l,v in res.items():
            result.append(v)
        return result


