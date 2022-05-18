class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for l in range(len(s)-9):
            d = s[l:l+10]
            if d in seen:
                res.add(d)
            seen.add(d)
        return list(res)