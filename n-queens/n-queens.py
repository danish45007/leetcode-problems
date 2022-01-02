class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        col = set()
        pos_diagonal = set() #r+c
        neg_diagonal = set() #r-c
        board = [['.']*n for i in range(n)]
        
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if (c in col or (row+c) in pos_diagonal or (row-c) in neg_diagonal):
                    continue
                
                col.add(c)
                pos_diagonal.add(row+c)
                neg_diagonal.add(row-c)
                board[row][c] = 'Q'
                
                backtrack(row+1)
                
                col.remove(c)
                pos_diagonal.remove(row+c)
                neg_diagonal.remove(row-c)
                board[row][c] = '.'
            
        backtrack(0)
        return result
            
                
        