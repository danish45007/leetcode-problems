class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
            optimizing the space
            Time: O(nm)
            Space: O(1)
        '''
        ROW = len(board)
        COL = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
        def live_neighbours(r,c):
            count = 0
            for d in directions:
                dir_r,dir_c = d
                row,col = r+dir_r,c+dir_c
                # out of bound 
                if (row == r and col == c) or row < 0 or row == ROW or col < 0 or col == COL:
                    continue
                if board[row][col] in [1,3]:
                    count += 1
            return count
        # mapping into cell into [0,1,2,3]
        for r in range(ROW):
            for c in range(COL):
                live_neighbour_count = live_neighbours(r,c)
                print([r,c],live_neighbour_count)
                # current cell already live
                if board[r][c]:
                    if live_neighbour_count in [2,3]:
                        board[r][c] = 3
                elif live_neighbour_count == 3:
                    board[r][c] = 2
        # reverse mapping
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
#         ROW = len(board)
#         COL = len(board[0])
#         board_copy = board[:]
#         directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
#         def live_or_die(row,col):
#             living = board[row][col]
#             for d in directions:
#                 dir_r,dir_c = d
#                 r,c = row+dir_r,col+dir_c
#                 # check in bound condition
#                 if(r < 0 or r == ROW or c < 0 or c == COL):
#                     continue
#                 if board[r][c]:
#                     living += 1
#             # if inital state is living 1
#             # lives if neighbour are 2 or 3
#             # else dies
#             if (board[row][col] and (living == 2 or living == 3)):
#                 return True
#             elif (not board[row][col] and living == 3):
#                 return True
#             else:
#                 return False
                                        
#         for r in range(ROW):
#             for c in range(COL):
#                 if(live_or_die(r,c)):
#                     board_copy[r][c] = int(not board[r][c])
#         board_copy = board
        
    

            
        
    
                
        