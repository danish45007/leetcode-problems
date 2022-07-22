class Solution:
    def maxPower(self, s: str) -> int:
        count,res = 1,1
        for idx in range(len(s)-1):
            if s[idx] == s[idx+1]:
                count +=1
            else:
                count = 1
            res = max(res,count)
        return res