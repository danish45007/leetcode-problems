class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        # check the edge case
        if grid[0][0] != 0 or grid[ROWS-1][COLS-1] != 0 : return -1
        queue = deque() #[x,y,curr_len]
        # adding the start position
        queue.append([0,0,1])
        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
        while queue:
            x,y,curr_len = queue.popleft()
            if (x,y) == (ROWS-1,COLS-1):
                return curr_len
            for x_inc,y_inc in directions:
                new_x,new_y = x+x_inc,y+y_inc
                # checking the boundary condition
                if new_x < 0 or new_y < 0 or new_x == ROWS or new_y == COLS or grid[new_x][new_y] != 0 or (new_x,new_y) in visited:
                    continue
                visited.add((new_x,new_y))
                queue.append([new_x,new_y,curr_len+1])
        return -1
                
        