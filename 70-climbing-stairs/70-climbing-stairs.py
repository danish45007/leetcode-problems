class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(n):
            if n == 0:
                return 
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in dp:
                return dp[n]
            dp[n] = helper(n-2)+helper(n-1)
            return dp[n]
        return helper(n)