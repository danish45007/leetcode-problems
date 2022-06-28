class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {} #{step:min_cost}
        def helper(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            if n in dp:
                return dp[n]
            one_step_cost = helper(n-1)+cost[n]
            two_step_cost = helper(n-2)+cost[n]
            min_cost = min(one_step_cost,two_step_cost)
            dp[n] = min_cost
            return dp[n]
        return min(helper(len(cost)-1),helper(len(cost)-2))

