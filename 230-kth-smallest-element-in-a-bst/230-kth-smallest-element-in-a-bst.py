# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr_node = root
        processed = 0
        while True:       
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            processed +=1

            if processed == k:
                return curr_node.val
            if curr_node:
                curr_node = curr_node.right
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def dfs(node): 
        #     return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        # nums = dfs(root)
        # for i in range(len(nums)):
        #     if i == k-1:
        #         return nums[i]
        
        
        # n = 0
        # stack = []
        # curr = root
        # # inorder traversal
        # while True:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     # reached end of left side
        #     curr = stack.pop()
        #     n += 1
        #     if n == k:
        #         return curr.val
        #     # add right for processing
        #     curr = curr.right
            