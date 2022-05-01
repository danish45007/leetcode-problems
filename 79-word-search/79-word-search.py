class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        visited = set()
        def dfs(r,c,i):
            # found all char in target word
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = (dfs(r,c+1,i+1) or dfs(r,c-1,i+1) or dfs(r+1,c,i+1) or dfs(r-1,c,i+1))
            # remove the curr r,c from visited after making 4 calls
            visited.remove((r,c))
            return res
            
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False