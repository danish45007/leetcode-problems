class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def lcs_bottom_up(s1,s2,n,m):
            count = 0
            dp = [[-1 for i in range(m+1)]  for j in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 0
            for i in range(n+1):
                for j in range(m+1):
                    count = max(count,dp[i][j])
            return count
        return lcs_bottom_up(nums1,nums2,len(nums1),len(nums2))
        
    