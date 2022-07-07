class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROW, COL = len(grid), len(grid[0])
        res = [[0]*COL for i in range(ROW)]
        def row_col_to_index(r,c):
            return ((r*COL +c)+k)%(ROW*COL)
        def index_to_row_col(idx):
            return [idx//COL,idx%COL]
        for r in range(ROW):
            for c in range(COL):
                new_index=row_col_to_index(r,c)
                new_r,new_j=index_to_row_col(new_index)
                res[new_r][new_j]=grid[r][c]
        return res
            