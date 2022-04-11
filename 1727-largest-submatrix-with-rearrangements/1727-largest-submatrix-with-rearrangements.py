class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        for r in range(1,row):
            for c in range(col):
                if(matrix[r][c] == 1):
                    matrix[r][c] += matrix[r-1][c]
                else:
                    matrix[r][c] = matrix[r][c]
        for r in range(row):
            matrix[r].sort(reverse=True)
            for c in range(col):
                res = max(res,(c+1)*matrix[r][c])
        return res
                