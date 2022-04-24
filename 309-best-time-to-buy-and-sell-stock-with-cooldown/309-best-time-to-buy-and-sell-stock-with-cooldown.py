class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,can_buy):
            # reached leaf node after that out of bound case
            if i >= len(prices):
                return 0
            # decision aready cached
            if (i,can_buy) in dp:
                return dp[(i,can_buy)]
            if can_buy:
                buy = dfs(i+1,not can_buy) - prices[i]
                cooldown = dfs(i+1,can_buy)
                dp[(i,can_buy)] = max(buy,cooldown)
            else:
                sell = dfs(i+2,not can_buy) + prices[i]
                cooldown = dfs(i+1,can_buy)
                dp[(i,can_buy)] = max(sell,cooldown)
            return dp[(i,can_buy)]
        return dfs(0,True)
            