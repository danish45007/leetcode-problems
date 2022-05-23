class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # from the start of the endpoint we can move in all 8 directions
        # assuming start of endpoint is at [0,0]
        directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
        ROW = len(board)
        COL = len(board[0])
         # marking the start of the endpoint with the mark_color
        board[rMove][cMove] = color
        
        def is_move_legal(start_endpoint_row,start_endpoint_col,direction,mark_color):
            # moving along the direction
            dir_r,dir_c = direction
            row = start_endpoint_row + dir_r
            col = start_endpoint_col + dir_c
            length = 1
            
            while(row >= 0 and row < ROW and col >= 0 and col < COL):
                length += 1
                # when reached empty cell
                if board[row][col] == '.': return False
                
                # check when reached end of the endpoint
                if board[row][col] == mark_color:
                    # return True is covered atleast 3 cells
                    return length >= 3
                
                # updating the row and col along dir
                row += dir_r
                col += dir_c
            return False
        
        # calling the is_move_legal in all directions
        for _dir in directions:
            if(is_move_legal(rMove,cMove,_dir,color)): return True
        return False
        
        