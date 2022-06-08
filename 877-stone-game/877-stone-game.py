class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # choices Alice has to start first so she can starting piking even or odd numbers
        # and as the overall sum of the stones is odd therefore sum of even != sum of odd
        # implies either even is greater or odd is greater
        
        dp = {} # {subarray[l:r]: max of alice}
        
        # @ returns: max alice can pick
        def dfs(l,r):
            if l > r: return 0
            if (l,r) in dp: return dp[(l,r)]
            
            # if alices start picking 
            # in alices turn of picking there will be even stones in array
            # in bob's turn there will be odd stones in array
            is_even = True if (r-l)%2 else False
            left_pick = piles[l] if is_even else 0
            right_pick = piles[r] if is_even else 0
            
            # if alice's pick left stone
            # dfs will be called on the remaining subarray
            left = dfs(l+1,r) + left_pick
            
            # if alice's pick right stone
            # dfs will be called on the remaining subarray
            
            right = dfs(l,r-1) + right_pick
            
            # consider the max of left and right
            
            dp[(l,r)] = max(left,right)
            return dp[(l,r)]
        return dfs(0,len(piles)-1) > sum(piles) // 2
            
            
            
            
                 
                