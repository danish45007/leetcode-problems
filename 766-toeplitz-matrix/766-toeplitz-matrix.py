class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def is_diagonal_unival(row,col):
            curr_val = matrix[row][col]
            while row < ROWS and col < COLS:
                if matrix[row][col] != curr_val:
                    return False
                
                row +=1
                col +=1
            return True
        
        
        for col in range(COLS):
            if not is_diagonal_unival(0,col):
                return False
            
        for row in range(1,ROWS):
            if not is_diagonal_unival(row,0):
                return False
        return True