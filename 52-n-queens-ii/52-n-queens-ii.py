class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col_set = set()
        right_diagonal_set = set() # (r-c) constant difference 
        left_diagonal_set = set() # (r+c) constant sum
        def backtrack(r):
            nonlocal res
            if r == n:
                return True
            for c in range(n):
                if c in col_set or (r+c) in left_diagonal_set or (r-c) in right_diagonal_set:
                    continue
                col_set.add(c)
                left_diagonal_set.add(r+c)
                right_diagonal_set.add(r-c)
                if backtrack(r+1):
                    res +=1
                col_set.remove(c)
                left_diagonal_set.remove(r+c)
                right_diagonal_set.remove(r-c)
            return False
                
        backtrack(0)
        return res