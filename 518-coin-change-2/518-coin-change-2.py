class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(index,curr_amount):
            # base case
            if curr_amount == amount:
                return 1
            if curr_amount > amount:
                return 0
            if index == len(coins):
                return 0
            
            if((index,curr_amount) in cache):
                return cache[(index,curr_amount)]
            
            res = dfs(index,curr_amount + coins[index]) + dfs(index+1,curr_amount)
            cache[(index,curr_amount)] = res
            return res
        return dfs(0,0)