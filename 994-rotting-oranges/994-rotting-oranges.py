class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        time,fresh = 0,0
        rotton = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]] 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    rotton.append([r,c])
        # bfs traversal
        while rotton and fresh > 0:
            for i in range(len(rotton)):
                # get the rotton orange
                r,c = rotton.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    # check for the bound condition
                    if(row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    # transform into rotton
                    grid[row][col] = 2
                    #append the recent rotton oranges into rotton queue
                    rotton.append([row,col])
                    fresh -=1
            time +=1
        return time if fresh == 0 else -1
        
        
        
        
        
                