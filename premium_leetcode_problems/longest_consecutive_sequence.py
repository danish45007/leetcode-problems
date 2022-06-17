'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example 1:

Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output:3
Explanation:
Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:
   2
    \
     3
    / 
   2    
  / 
 1
Output:2
Explanation:
Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.

'''

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive(self, root: TreeNode) -> int:
        self.longest_seq = 1
        self.dfs(root,root.val-1,0)
        return self.longest_seq
    
    def dfs(self,curr_node,prev_val,curr_len):
        if curr_node:
            if curr_node.val - 1 == prev_val:
                curr_len +=1
                self.longest_seq = max(self.longest_seq,curr_len)
                self.dfs(curr_node.left,curr_node.val,curr_len)
                self.dfs(curr_node.right,curr_node.val,curr_len)
            else:
                self.dfs(curr_node.left,curr_node.val,1)
                self.dfs(curr_node.right,curr_node.val,1)
