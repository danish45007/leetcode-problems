# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def back_track(n):
            res = []
            # empty tree -> no tree will be formed
            if n == 0:
                return []
            # only root node 1 tree will be formed
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            for left in range(n):
                right = n - left - 1
                left_tree,right_tree = back_track(left),back_track(right)
                for t1 in left_tree:
                    for t2 in right_tree:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res
            return res
        return back_track(n)