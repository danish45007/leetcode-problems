class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited  = set((0,0,k)) #{r,c,curr_k}
        queue = deque()
        queue.append((0,0,0,k))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        if k >= (ROWS-1) + (COLS-1):
            return ROWS+COLS-2
        while queue:
            x,y,curr_len,k_remaining = queue.popleft()
            if x == ROWS-1 and y == COLS-1:
                return curr_len
            for x_inc,y_inc in directions:
                new_x,new_y = x+x_inc,y+y_inc
                # checking the boundary condition
                if  new_x < 0 or new_x == ROWS or new_y < 0 or new_y == COLS or (new_x,new_y,k_remaining) in visited:
                    continue
                new_remaining = k_remaining - grid[new_x][new_y]
                if new_remaining >= 0 and (new_x,new_y,new_remaining) not in visited:
                    visited.add((new_x,new_y,new_remaining))
                    queue.append((new_x,new_y,curr_len+1,new_remaining))
        return -1