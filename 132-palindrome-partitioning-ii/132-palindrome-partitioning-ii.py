class Solution:
    @cache
    def valid(self, i, j):
        if i>=j:
            return True
        return (self.s[i] == self.s[j]) and self.valid(i+1, j-1)
    
    @cache
    def backtrack(self, i, k):
        memo = {}
        if i>=k:
            return 0
        min_cuts = float('inf')
        for j in range(i, k+1):
            if (i,j) in memo:
                if j<k:
                    min_cuts = min(min_cuts, 1 + self.backtrack(j+1, k))
                else:
                    min_cuts = min(min_cuts, 0)
            else:
                if self.valid(i, j):
                    memo[(i,i)] = True
                    if j<k:
                        min_cuts = min(min_cuts, 1 + self.backtrack(j+1, k))
                    else:
                        min_cuts = min(min_cuts, 0)
        return min_cuts

    def minCut(self, s: str) -> int:
        self.s = s
        res = self.backtrack(0, len(s)-1)
        return res