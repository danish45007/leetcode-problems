class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         row,col = len(heights),len(heights[0])
#         pacific,atlantic = set(),set()
#         result = []
#         def dfs(r,c,visited,prev_height):
#             # base case for the dfs
#             # Note as we are traversing in opposite direction that is from outward => inwards thats
#             # why the oppisite condition prev_height > heights[r][c]
#             if(r < 0 or c < 0 or r >= row or c >= col or (r,c) in visited or prev_height > heights[r][c]):
#                 return
#             visited.add((r,c))
#             dfs(r,c+1,visited,heights[r][c])
#             dfs(r,c-1,visited,heights[r][c])
#             dfs(r+1,c,visited,heights[r][c])
#             dfs(r-1,c,visited,heights[r][c])
            
            
#         # traversing over diff col. for first row(pacific) and last row(atlantic)
#         for c in range(col):
#             # to reach pacific
#             dfs(0,c,pacific,heights[0][c])
#             # to reach atlantic
#             dfs(row-1,c,atlantic,heights[row-1][c])
#         # traversing over diff row values for first col(pacific) and last col(atlantic)
#         for r in range(row):
#             # to reach pacific
#             dfs(r,0,pacific,heights[r][0])
#             # to reach atlantic
#             dfs(r,col-1,atlantic,heights[r][col-1])
        
#         for r in range(row):
#             for c in range(col):
#                 # taking the interstion for the sets
#                 if((r,c) in pacific and (r,c) in atlantic):
#                     result.append([r,c])
#         return result
        
        ROWS,COLS = len(heights),len(heights[0])
        pacific_set,atlantic_set = set(),set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,visited,prev_height):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or prev_height > heights[r][c]:
                return
            visited.add((r,c))
            for inc_row,inc_col in directions:
                next_row,next_col = r+inc_row,c+inc_col
                dfs(next_row,next_col,visited,heights[r][c])
        
        # for top and bottom ocean corner
        for c in range(COLS):
            # for pacific
            dfs(0,c,pacific_set,heights[0][c])
            # for atlanctic
            dfs(ROWS-1,c,atlantic_set,heights[ROWS-1][c])
        
        # for left and right ocean corner
        for r in range(ROWS):
            # for pacific
            dfs(r,0,pacific_set,heights[r][0])
            # for atlantic
            dfs(r,COLS-1,atlantic_set,heights[r][COLS-1])
        
        
        # find the interction
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    res.append((r,c))
        return res
        
        
            
                    