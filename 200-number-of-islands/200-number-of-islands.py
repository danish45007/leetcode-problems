class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or (r,c) in visit or grid[r][c]=='0':
                return
            
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visit:
                    dfs(i,j)
                    ans+=1
        return ans
        
        
        
    
    
                