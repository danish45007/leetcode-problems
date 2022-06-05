class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]
        col_set = set()
        right_diagonal_set = set() # (r-c) constant difference 
        left_diagonal_set = set() # (r+c) constant sum
        def backtrack(r):
            nonlocal res
            if r == n:
                board_copy = ["".join(row) for row in board]
                res.append(board_copy)
                return
            for c in range(n):
                if c in col_set or (r+c) in left_diagonal_set or (r-c) in right_diagonal_set:
                    continue
                col_set.add(c)
                left_diagonal_set.add(r+c)
                right_diagonal_set.add(r-c)
                board[r][c] = 'Q'
                
                backtrack(r+1)
                
                col_set.remove(c)
                left_diagonal_set.remove(r+c)
                right_diagonal_set.remove(r-c)
                board[r][c] = '.'
                
                
        
        backtrack(0)
        return res