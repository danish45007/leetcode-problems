class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp = [0]*(n+1)
        # offset = 1
        # for i in range(1,n+1):
        #     if offset*2 == i:
        #         offset = i
        #     dp[i] = 1 + dp[i-offset]
        # return dp
        
        dp = [0]*(n+1)
        offset = 1
        for num in range(1,n+1):
            # update the offset
            if offset * 2 == num:
                offset = offset * 2
            dp[num]  = 1 + dp[num-offset]
        return dp
            