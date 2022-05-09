class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[float('inf') for i in range(m+1)] for j in range(n+1)]
        # word1 is empty
        for i in range(m+1):
            dp[n][i] = m-i
        for j in range(n+1):
            dp[j][m] = n-j
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]