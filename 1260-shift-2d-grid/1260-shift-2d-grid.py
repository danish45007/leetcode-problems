class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                one=((r*n +c)+k)%(m*n)
                new_r,new_j=one//n, one%n
                ans[new_r][new_j]=grid[r][c]
        return ans
            