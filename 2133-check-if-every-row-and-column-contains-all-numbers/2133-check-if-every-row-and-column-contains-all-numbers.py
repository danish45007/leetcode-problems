class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        valid_set_of_numbers = [i for i in range(1,len(matrix)+1)]
        row_visited = defaultdict(set)
        col_visited = defaultdict(set)
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if(
                   matrix[r][c] in row_visited[r] or 
                   matrix[r][c] in col_visited[c]):
                    return False
                row_visited[r].add(matrix[r][c])
                col_visited[c].add(matrix[r][c])
        return True