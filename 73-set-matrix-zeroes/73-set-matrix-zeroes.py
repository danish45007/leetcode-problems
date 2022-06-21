class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS,COLS = len(matrix),len(matrix[0])
        zero_row = False
        
        # marking the cell that need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # the column 0 
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero_row = True
        
        # actually marking the r,c that need to be zeroed out
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # marking the 0th row and 0th column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if zero_row == True:
            for c in range(COLS):
                matrix[0][c] = 0 