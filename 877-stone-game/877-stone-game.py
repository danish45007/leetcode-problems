class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # choices Alice has to start first so she can starting piking even or odd numbers
        # and as the overall sum of the stones is odd therefore sum of even != sum of odd
        # implies either even is greater or odd is greater
        
        
        dp = {} #((l,r): max_sum)
        def dfs(l,r):
            if r - l == n:
                return 
            if (l,r) in dp :
                return dp[(l,r)]
        
        return True
            
            
                 
                