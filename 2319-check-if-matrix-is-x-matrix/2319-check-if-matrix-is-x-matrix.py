class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        grid_size = len(grid)
        diagonals = set()
        start_col,end_col = 0,grid_size-1
        size = grid_size
        while size > 0:
            diagonals.add((start_col,end_col))
            start_col +=1
            end_col -=1
            size -=1
        for i in range(grid_size):
            for j in range(grid_size):
                if i == j or (i,j) in diagonals:
                    if grid[i][j] == 0:
                        return False
                elif i != j and (i,j) not in diagonals:
                    if grid[i][j] != 0:
                        return False
        return True