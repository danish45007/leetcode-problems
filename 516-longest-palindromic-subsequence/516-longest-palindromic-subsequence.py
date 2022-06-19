class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def lcs(s1,s2,n,m):
            if n == len(s1) or m == len(s2):
                return 0
            if (n,m) in dp:
                return dp[(n,m)]
            if s1[n] == s2[m]:
                dp[(n,m)] = 1 + lcs(s1,s2,n+1,m+1)
            else:
                dp[(n,m)] = max(lcs(s1,s2,n+1,m),lcs(s1,s2,n,m+1))
            return dp[(n,m)]
        return lcs(s,s[::-1],0,0)