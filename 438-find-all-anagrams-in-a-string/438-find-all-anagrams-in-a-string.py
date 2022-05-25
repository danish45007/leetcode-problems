class Solution:
    def findAnagrams(self, s: str, p: str) -> int:
        return self.sliding_window_solution(p,s)
    
    def sliding_window_solution(self,pattern, txt):
        i,j = 0,0
        res = []
        pattern_map = {} #{char: count}
        for char in pattern:
            pattern_map[char] = 1 + pattern_map.get(char,0)
        count = len(pattern_map)
        # window size
        k = len(pattern)
        while j < len(txt):
            # if current char in map reduce the count
            if txt[j] in pattern_map:
                pattern_map[txt[j]] -=1
                # no char in for the next window
                if pattern_map[txt[j]] == 0:
                    count -=1
            # reached the window
            if j-i+1 == k:
                if count == 0:
                    res.append(i)
                if txt[i] in pattern_map:
                    pattern_map[txt[i]] += 1
                    if pattern_map[txt[i]] == 1:
                        count+=1
                i+=1
            j +=1
        return res
            
                
            
    