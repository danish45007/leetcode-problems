class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(target):
            if target == 0:
                return 1
            if target < 1:
                return 0
            
            if target in dp:
                return dp[target]
            _sum = 0
            for num in nums:
                _sum += dfs(target-num)
            dp[target] = _sum
            return dp[target]
        return dfs(target)