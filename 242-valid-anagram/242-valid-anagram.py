class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map,t_map = {},{}
        for char in s:
            s_map[char] = 1 + s_map.get(char,0)
        for char in t:
            t_map[char] = 1 + t_map.get(char,0)
        for key in s_map:
            if key not in t_map or s_map[key] != t_map[key]:
                return False
        return True
            