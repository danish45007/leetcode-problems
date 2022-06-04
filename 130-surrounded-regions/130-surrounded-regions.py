class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        # 1. capture the unsurrounded region with 'T' ('O' -> 'T')
        # cell in the unsurrounded region are on the 0th row,col or last row,col
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" 
                    and (r in [0, ROWS-1] or c in [0, COLS-1])):
                    dfs(r,c)
        
        # 2. capture the surrounded region mark 'O' -> 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        # 3. uncapture the ununsurrounded region 'T' -> 'O'
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'