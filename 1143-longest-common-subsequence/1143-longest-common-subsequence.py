class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs_bottom_up(s1,s2,n,m):
            dp = [[-1 for i in range(m+1)]  for j in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            return dp[n][m]
        return lcs_bottom_up(text1,text2,len(text1),len(text2))