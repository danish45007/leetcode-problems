class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        res_length = 0
                          
        for i in range(len(s)):
            # in case odd length palindrome
            left,right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if((right-left+1) > res_length):
                    result = s[left:right+1]
                    res_length = right-left+1
                left -=1
                right +=1
            # in case of even length palindrome
            left,right = i,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if((right-left+1) > res_length):
                    result = s[left:right+1]
                    res_length = right-left+1
                left -=1
                right +=1
            
            
        return result
            
            