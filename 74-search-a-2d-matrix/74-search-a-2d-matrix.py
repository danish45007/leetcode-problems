class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(n+m)
        # n,m = len(matrix),len(matrix[0])
        # i,j = 0,m-1
        # while (i >= 0 and i < n and j >= 0 and j < m):
        #     if(matrix[i][j] == target):
        #         return True
        #     elif(target < matrix[i][j]):
        #         j -=1
        #     elif(target > matrix[i][j]):
        #         i +=1
        # return False
        
        # O(logN + logM)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # calculate the row where target can be found
        start_row = 0
        end_row = ROWS-1
        
        while start_row <= end_row:
            mid_row = (start_row+end_row)//2
            if target > matrix[mid_row][-1]:
                start_row = mid_row+1
            elif target < matrix[mid_row][0]:
                end_row = mid_row-1
            else:
                break
        if not (start_row <= end_row):
            return False
        target_row = (start_row+end_row)//2
        start_col = 0
        end_col = COLS-1
        while start_col <= end_col:
            mid_col = (start_col+end_col)//2
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] > target:
                end_col = mid_col-1
            else:
                start_col = mid_col+1
        return False
        