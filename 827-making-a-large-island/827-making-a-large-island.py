class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # step 1 : To convert the grid into pre-computed sum of group of island and map the unique group island id with
        # its area
        unique_island_id = -1
        island_id_to_area_map = {}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def group_sum_area(r,c):
            if  0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = unique_island_id
                area = 1
                for inc_r,inc_c in directions:
                    new_r,new_c = r + inc_r,c + inc_c
                    area += group_sum_area(new_r,new_c)
                return area
            else:
                return 0
            
        
        for r in range(ROWS):
            for c in range(COLS):
                # if its a land
                if grid[r][c] == 1:
                    island_area = group_sum_area(r,c)
                    island_id_to_area_map[unique_island_id] = island_area 
                    unique_island_id -=1
                    
        max_area = 0
        # step:2 check for 0 cell and add its surrounding areas
        for r in range(ROWS):
            for c in range(COLS):
                # if cell 0 only
                if not grid[r][c]:
                    area = 1
                    surrounding = set()
                    for inc_r,inc_c in directions:
                        new_r,new_c = r + inc_r,c + inc_c
                        if (0 <= new_r < ROWS) and  (0 <= new_c < COLS) and grid[new_r][new_c] != 0:
                            surrounding.add(grid[new_r][new_c])
                        
                    for s in surrounding:
                        area += island_id_to_area_map[s]
                    max_area = max(area,max_area)
        return max_area if max_area else ROWS*COLS