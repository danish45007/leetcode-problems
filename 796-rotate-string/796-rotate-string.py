class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        for i in range(1, len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
            