class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        No need to keep track of time variable as time is directly proportional to height as mentioned in the problem
        finally return in the min height in the path from (0,0) -> (N-1,N-1)
        '''
        N = len(grid)
        visited = set()
        min_heap = [[grid[0][0],0,0]]  #[height,row,col]
        visited.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]] # all possible 4 directions
        while min_heap:
            height,row,col = heapq.heappop(min_heap)
            # reached target
            if row == N-1 and col == N-1:
                return height
            # visiting all 4 direction 
            for dir_row,dir_col in directions:
                neighbour_row,neighbour_col = row + dir_row, col + dir_col
                # in bound check for new row and col
                if(neighbour_row < 0 or neighbour_col < 0 or neighbour_row == N or neighbour_col == N or (neighbour_row,neighbour_col) in visited):
                    continue
                # making sure keeping the max height(potential min. height) within path
                new_min_height = max(height,grid[neighbour_row][neighbour_col])
                heapq.heappush(min_heap,[new_min_height,neighbour_row,neighbour_col])
                visited.add((neighbour_row,neighbour_col))
                
                
            
        