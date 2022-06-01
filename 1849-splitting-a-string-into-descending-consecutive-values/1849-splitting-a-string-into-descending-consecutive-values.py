class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(idx,prev_val):
            if idx == len(s):
                return True
            for j in range(idx,len(s)):
                val = int(s[idx:j+1])
                if prev_val-val == 1 and dfs(j+1,val):
                    return True
            return False
        
        # len(s)-1 to to keep atleast 2 int values
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1,val):
                return True
        return False