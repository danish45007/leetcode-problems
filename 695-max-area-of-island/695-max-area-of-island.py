class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        def helper_dfs(i,j):
            # boundary case
            if (i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0 or (i,j) in visited):
                return 0
            visited.add((i,j))
            return (1 + helper_dfs(i+1,j) + helper_dfs(i-1,j) + helper_dfs(i,j+1) +helper_dfs(i,j-1))
        
        for i in range(row):
            for j in range(col):
                max_area = max(max_area,helper_dfs(i,j))
        return max_area
                        