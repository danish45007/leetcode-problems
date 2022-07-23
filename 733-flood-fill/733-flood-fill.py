class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        base_color = image[sr][sc]
        visited = set()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or image[r][c] != base_color:
                return
            image[r][c] = newColor
            visited.add((r,c))
            for row_inc,col_inc in directions:
                new_row,new_col = r+row_inc,c+col_inc
                dfs(new_row,new_col)
        dfs(sr,sc)
        return image