class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float('inf')
            for day,cost in zip([1,7,30],costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                res = min(dp[i],cost+dfs(j))
                dp[i] = res
            return res
        return dfs(0)
                
        