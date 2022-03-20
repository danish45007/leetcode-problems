class Solution:
    def findAnagrams(self, s: str, p: str) -> int:
        return self.search(p,s)
    
    def search(self,pat, txt):
        i,j = 0,0
        res = []
        pattern_map = {}
        for char in pat:
            if(char in pattern_map):
                pattern_map[char] += 1
            else:
                pattern_map[char] = 1
        count = len(pattern_map)
        k = len(pat)
        while j < len(txt):
            if(txt[j] in pattern_map):
                pattern_map[txt[j]] -=1
                if(pattern_map[txt[j]] == 0):
                    count -=1 
            if(j-i+1 < k):
                j +=1
            elif(j-i+1 == k):
                if(count == 0):
                    res.append(i)
                if(txt[i] in pattern_map):
                    pattern_map[txt[i]] +=1
                    if(pattern_map[txt[i]] == 1):
                        count +=1
                i +=1
                j +=1
        return res
            
    