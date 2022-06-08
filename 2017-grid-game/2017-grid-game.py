class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        COL = len(grid[0])
        pref_row1 = grid[0].copy()
        pref_row2 = grid[1].copy()
        
        for i in range(1,COL):
            pref_row1[i] += pref_row1[i-1]
            pref_row2[i] += pref_row2[i-1]
        
        res = float('inf')
        for i in range(COL):
            top = pref_row1[-1] - pref_row1[i]
            bottom = pref_row2[i-1] if i > 0 else 0
            second_robo = max(top,bottom)
            res = min(res,second_robo)
        return res