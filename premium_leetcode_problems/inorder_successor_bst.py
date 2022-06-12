'''
Description
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

Example
Example 1:

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
Example 2:

Input: {2,1,3}, node with value 1
Output: 2
Explanation: 
    2
   / \
  1   3

'''

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        successor = None
        curr_node = root
        while curr_node:
            if curr_node.val <= p.val:
                curr_node = curr_node.right
            else:
                successor = curr_node
                curr_node = curr_node.left
        return successor