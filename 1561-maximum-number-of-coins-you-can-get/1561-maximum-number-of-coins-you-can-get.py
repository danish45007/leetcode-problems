class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = 0
        i,j = len(piles)-2,0
        while j < len(piles)//3:
            max_coin += piles[i]
            i -=2
            j +=1
        return max_coin
        
            
            