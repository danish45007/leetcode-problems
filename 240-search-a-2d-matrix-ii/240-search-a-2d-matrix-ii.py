class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i,j = 0,col-1
        while i >= 0 and i < row and j >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                 j -=1
            elif target > matrix[i][j]:
                i +=1
        return False