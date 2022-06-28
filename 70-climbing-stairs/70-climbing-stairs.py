class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def helper(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in dp:
                return dp[n]
            steps = helper(n-2)+helper(n-1)
            dp[n] = steps
            return steps
        return helper(n)