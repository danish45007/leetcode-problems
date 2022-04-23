class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy,sell = 0,1
        while sell < len(prices):
            # potential selling prices that can generate profit
            if(prices[sell] > prices[buy]):
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
            else:
                buy = sell
            
            sell +=1
        return max_profit
        
        
                