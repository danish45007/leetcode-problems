class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        def get_max_col(row):
            max_val = 0
            max_col = 0
            for col in range(len(mat[0])):
                if mat[row][col] > max_val:
                    max_col = col
                    max_val = mat[row][col]
            return max_col
        
        start = 0
        end = len(mat)-1
        while start <= end:
            mid_row = (start+end)//2
            max_col = get_max_col(mid_row)
            if mid_row == 0:
                if mat[mid_row][max_col] > mat[mid_row+1][max_col]:
                    return [mid_row,max_col]
            if mid_row == len(mat)-1:
                if mat[mid_row][max_col] > mat[mid_row-1][max_col]:
                    return [mid_row,max_col]
            else:
                if mat[mid_row][max_col] > mat[mid_row+1][max_col] and mat[mid_row][max_col] > mat[mid_row-1][max_col]:
                    return [mid_row,max_col]
            
            if mat[mid_row][max_col] < mat[mid_row+1][max_col]:
                start = mid_row+1
            else:
                end = mid_row-1
        return [-1,-1]
                   
                