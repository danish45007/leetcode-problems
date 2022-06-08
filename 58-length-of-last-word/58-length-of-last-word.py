class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s)-1
        while s[i] == " ":
            i -=1
        # reached the first valid char
        while i >= 0 and s[i] != " ":
            res += 1
            i -=1
        return res
                