class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])
        self.pref_sum_matrix = [[0 for i in range(COL+1)] for j in range(ROW+1)]
        # populating pref sum for each cell in pref_sum_matrix
        for r in range(ROW):
            pref_sum = 0
            for c in range(COL):
                # offsetting it by 1 as the 0th row and 0th col in filled the 0's
                pref_sum += matrix[r][c]
                above_cell = self.pref_sum_matrix[r][c+1]
                self.pref_sum_matrix[r+1][c+1] = pref_sum + above_cell

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2 = row1+1,row2+1
        col1,col2 = col1+1,col2+1
        bottom_right = self.pref_sum_matrix[row2][col2]
        above = self.pref_sum_matrix[row1-1][col2]
        left = self.pref_sum_matrix[row2][col1-1]
        top_left = self.pref_sum_matrix[row1-1][col1-1]
        return bottom_right - above - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)