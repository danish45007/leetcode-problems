class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        if(s == t):
            return s
        s_map,t_map = {},{}
        for char in t:
            t_map[char] = 1 + t_map.get(char,0)
        
        have,need = 0,len(t_map)
        result,result_len = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r],0)
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have +=1
            # after hitting the first window     
            while have == need:
                # we will get answer here
                if(r-l+1) < result_len:
                    result = [l,r]
                    result_len = r-l+1
                # try to optimize the current window solution
                s_map[s[l]] -=1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -=1
                l +=1
        l,r = result
        return s[l:r+1] if result_len != float("inf") else ""
            
            
            
        