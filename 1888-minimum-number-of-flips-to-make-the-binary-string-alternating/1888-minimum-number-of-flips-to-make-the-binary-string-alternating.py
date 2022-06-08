class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s =  s + s
        comb1 = ""
        comb2 = ""
        diff1,diff2 = 0,0
        for i in range(len(s)):
            comb1 += "0" if i % 2 else "1"
            comb2 += "1" if i % 2 else "0"
        res = float('inf')
        l = 0
        for r in range(len(s)):
            if s[r] != comb1[r]:
                diff1 += 1
            
            if s[r] != comb2[r]:
                diff2 += 1
            
            # window size exceed
            if (r-l+1) > n:
                # move the left pointer
                if s[l] != comb1[l]: diff1 -= 1
                if s[l] != comb2[l]: diff2 -= 1
                l +=1
            
            if (r-l+1) == n:
                res = min(res,diff1,diff2)
        return res
            
                
            
        