class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        i,j = 0,m-1
        while (i >= 0 and i < n and j >= 0 and j < m):
            if(matrix[i][j] == target):
                return True
            elif(target < matrix[i][j]):
                j -=1
            elif(target > matrix[i][j]):
                i +=1
        return False