class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            val = ord(char) - ord('A') + 1
            res = res*26 + val
        return res
            
            