class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROW, COL = len(grid), len(grid[0])
        res = [[0]*COL for i in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                new_index=((r*COL +c)+k)%(ROW*COL)
                new_r,new_j=new_index//COL, new_index%COL
                res[new_r][new_j]=grid[r][c]
        return res
            