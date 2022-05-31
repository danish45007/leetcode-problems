class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_code_set = set()
        l,r = 0,0
        while r < len(s):
            if r-l+1 == k:
                unique_code_set.add(s[l:r+1])
                l+=1
            r +=1
        return len(unique_code_set) == 2**k