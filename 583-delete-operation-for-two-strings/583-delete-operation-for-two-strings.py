class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} #(n,m) : lcs
        def lcs(s1,s2,n,m):
            if n == len(word1) or m == len(word2):
                return 0
            if (n,m) in dp:
                return dp[(n,m)]
            if s1[n] == s2[m]:
                dp[(n,m)] = 1 + lcs(s1,s2,n+1,m+1)
            else:
                dp[(n,m)] = max(lcs(s1,s2,n+1,m),lcs(s1,s2,n,m+1))
            return dp[(n,m)]
        return len(word1) + len(word2) - 2*(lcs(word1,word2,0,0))
        
        