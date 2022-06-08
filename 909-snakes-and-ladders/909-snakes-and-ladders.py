class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_size = len(board)
        # reverse the rows in the board
        board.reverse()
        # get the [row,col] from the given val at square
        def get_row_col(square):
            row = (square-1) // board_size
            col = (square-1) % board_size
            if row % 2:
                col = board_size - 1 - col
            return [row,col]
        
        # apply bfs
        # start from first sqaure and 0 move
        queue = deque() #[square,move]
        queue.append([1,0])
        visited = set()
        while queue:
            square,move = queue.popleft()
            # check for the possible values in dices (0,6)
            for i in range(1,7):
                next_square = square + i
                # get the r,c for the non -1
                r,c = get_row_col(next_square)
                if(board[r][c] != -1):
                    next_square = board[r][c]
                # check if reached target
                if next_square == (board_size*board_size):
                    return move + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append([next_square,move+1])
        return -1
                    
        
        