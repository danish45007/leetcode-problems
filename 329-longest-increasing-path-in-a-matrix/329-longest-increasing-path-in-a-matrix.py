class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp = {} #{(r,c) => LIP}
        def dfs(r,c,prev):
            # out of bound or non inc order base case
            if r < 0 or r == row or c < 0 or c == col or prev >= matrix[r][c]:
                return 0
            # if already calculated r,c
            if (r,c) in dp:
                return dp[(r,c)]
            
            # calculate the LIP
            # apply dfs in all 4 direction
            # atleast 1 if no LIP
            res = 1
            res = max(res,1 + dfs(r+1,c,matrix[r][c]))
            res = max(res,1 + dfs(r-1,c,matrix[r][c]))            
            res = max(res,1 + dfs(r,c-1,matrix[r][c]))            
            res = max(res,1 + dfs(r,c+1,matrix[r][c]))
            # cache result
            dp[(r,c)] = res
            return res
        
        for r in range(row):
            for c in range(col):
                dfs(r,c,-1)
        return max(dp.values())