class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0': 
            dp[1] = 1
        for i in range(2, len(s)+1):
            if 9 >= int(s[i-1]) >= 1:
                dp[i] += dp[i-1]
            second = int(s[i-2:i])
            if 26 >= second >= 10:
                dp[i] += dp[i-2]
        print(dp)
        return dp[-1]