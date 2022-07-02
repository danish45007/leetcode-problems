# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Initialize the cache
        cache = {}
        def helper(first, last):
			# If the value in cache return the trees possible directly from cache
            if (first, last) in cache:
                return cache[(first,last)]
			# When we reach the leaf node then just return None as there are no more possible trees from this point
            if first > last:
                return [None]
            trees = []
            
			# 1. Every value from 1 to n can be a root node
            for root in range(first, last+1):
				# 2. Iterate and add all the possible left sub trees to the current root.
                for left in helper(first, root - 1):
					# 3. Iterate and add all the possible right sub trees to the current root.
                    for right in helper(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
			# Add to cache to not repeat computations.
            cache[(first,last)] = trees
            return trees
		# Call the function with the base case to return the result
        return helper(1,n)