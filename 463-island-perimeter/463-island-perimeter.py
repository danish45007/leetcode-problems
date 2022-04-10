class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()        
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            p = dfs(r,c+1)
            p += dfs(r+1,c)
            p += dfs(r,c-1)
            p += dfs(r-1,c)
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)