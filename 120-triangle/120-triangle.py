class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        space: O(n)
        time: O(n^2)
        '''
        dp = [0]*(len(triangle)+1)
        for row in range(len(triangle)-1,-1,-1):
            for i,num in enumerate(triangle[row]):
                dp[i] = num + min(dp[i],dp[i+1])
        return dp[0]