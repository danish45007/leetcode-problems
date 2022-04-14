class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0': 
            dp[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            second = int(s[i-2:i])
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]
        return dp[-1]