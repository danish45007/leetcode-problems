class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # calculate the prefix sum for each row
        for row in range(ROWS):
            for col in range(1,COLS):
                matrix[row][col] += matrix[row][col-1]
        res = 0
        for col1 in range(COLS):
            for col2 in range(col1,COLS):
                lookup = {0:1}
                _sum = 0
                for r in range(ROWS):
                    _sum += matrix[r][col2] - (matrix[r][col1-1] if col1 > 0 else 0)
                    res += lookup.get(_sum-target,0)
                    lookup[_sum] = 1 + lookup.get(_sum,0)
        return res