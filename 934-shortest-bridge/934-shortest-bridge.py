class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # visited number of islands (1's)
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def row_col_invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N
        # apply dfs to get one of the island
        def dfs(r,c):
            if row_col_invalid(r,c) or not grid[r][c] or (r,c) in visited:
                return
            visited.add((r,c))
            for row,col in directions:
                dfs(r+row,c+col)
        
        # apply bfs to find the shortest path b/w islands (2 1's)
        def bfs():
            # added the (r,c) for 1st island into queue and applying bfs over there to find the min no of level to find the 2nd
            # island
            queue = deque(visited)
            result = 0
            while queue:
                queue_len = len(queue)
                for i in range(queue_len):
                    _row,_col = queue.popleft()
                    for r,c in directions:
                        row,col = _row+r,_col+c
                        if row_col_invalid(row,col) or (row,col) in visited:
                            continue
                        # found the nearst island
                        if grid[row][col]:
                            return result
                        queue.append((row,col))
                        visited.add((row,col))
                result += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    # place the first island in visited
                    dfs(r,c)
                    # returns the flips once find the min to connect 1 island with 2nd island
                    return bfs()
                    
            
            