class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = {} #{step:min_cost}
        # def helper(n):
        #     if n == 0:
        #         return cost[0]
        #     if n == 1:
        #         return cost[1]
        #     if n in dp:
        #         return dp[n]
        #     one_step_cost = helper(n-1)+cost[n]
        #     two_step_cost = helper(n-2)+cost[n]
        #     min_cost = min(one_step_cost,two_step_cost)
        #     dp[n] = min_cost
        #     return min_cost
        # return min(helper(len(cost)-1),helper(len(cost)-2))
        
        # bottom-up
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])
        
