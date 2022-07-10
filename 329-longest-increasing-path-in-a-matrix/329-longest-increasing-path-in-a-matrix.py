class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp = {} #{(r,c) => LIP}
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
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
            for inc_row,inc_col in directions:
                res = max(res,1+dfs(r+inc_row,c+inc_col,matrix[r][c]))
            # cache result
            dp[(r,c)] = res
            return res
        max_lip = float('-inf')
        for r in range(row):
            for c in range(col):
                max_lip = max(dfs(r,c,-1),max_lip)
        return max_lip