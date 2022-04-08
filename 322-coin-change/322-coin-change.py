class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for j in range(amount+1):
            dp[0][j] = float('inf') - 1
        for i in range(1,len(coins)+1):
            dp[i][0] = 0
        
        for i in range(1,amount+1):
            if(i%coins[0] != 0):
                dp[1][i] = float('inf')-1
            else:
                dp[1][i] = i / coins[0]
        
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if(coins[i-1] > j):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        if dp[len(coins)][amount] == float('inf'):
            return -1 
        else:
            return dp[len(coins)][amount]