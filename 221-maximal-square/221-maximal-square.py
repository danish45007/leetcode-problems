class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        max_side = 0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                    max_side = max(max_side,dp[i][j])
        return max_side**2
