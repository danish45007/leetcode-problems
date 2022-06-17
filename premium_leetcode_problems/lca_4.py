'''
given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pias a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node xto some leaf node.


Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

'''

def solve(root,nodes):
    nodes = set(nodes)
    def dfs(node):
        if not node:
            return None
        if node in nodes:
            return node
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            return node
        else:
            return left or right
    return dfs(root)