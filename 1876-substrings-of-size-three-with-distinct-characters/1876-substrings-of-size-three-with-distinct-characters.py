class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i,j = 0,0
        sub = []
        count = 0
        k=3
        while j < len(s):
            sub.append(s[j])
            if((j-i+1) < k):
                j += 1
            elif((j-i+1) == k):
                if(len(set(sub)) == len(sub)):
                    count += 1
                
                sub.pop(0)
                i+=1
                j+=1
        
        return count