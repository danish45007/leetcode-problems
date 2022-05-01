class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:return 1
        prev_count,prev_prev_count = 1,1
        for i in range(1,len(s)):
            single_digit = int(s[i])
            double_digit = int(s[i-1:i+1])
            curr_count = 0
            if (single_digit > 0):curr_count += prev_count
            if (double_digit >= 10 and double_digit <= 26):curr_count += prev_prev_count
            prev_prev_count = prev_count
            prev_count = curr_count
        return prev_count
                
            