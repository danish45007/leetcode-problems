class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board_state):
            ROWS = len(board)
            COLS = len(board[0])

            for r in range(ROWS):
                for c in range(COLS):
                    # cell to place a char from[1,9]
                    if board[r][c] == '.':
                        for char in range(1,10):
                            # valid state for char
                            if is_state_valid(r,c,str(char)):
                                # update the board state
                                board[r][c] = str(char)
                                # next call for new board state
                                if backtrack(board):
                                    return True
                                else:
                                    # undo the state to prev state
                                    board[r][c] = '.'
                        return False
            return True
        def is_state_valid(row,col,char):
            for i in range(0,9):
                # check for row
                if board[i][col] == char:
                    return False
                
                # check for col
                if board[row][i] == char:
                    return False
                
                # check for the sub matrix(3*3)
                if board[3*(row//3) + i // 3][3*(col//3) + i % 3] == char:
                    return False
            return True
        
        backtrack(board)