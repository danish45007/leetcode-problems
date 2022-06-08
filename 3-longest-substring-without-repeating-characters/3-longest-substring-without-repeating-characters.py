class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count_map = {}
        l,r = 0,0
        max_len = float('-inf')
        
        while r < len(s):
            char_count_map[s[r]] = 1 + char_count_map.get(s[r],0)
            if len(char_count_map) == r-l+1:
                max_len = max(max_len,r-l+1)
            if len(char_count_map) < r-l+1:
                while len(char_count_map) < r-l+1:
                    char_count_map[s[l]] -= 1
                    if char_count_map[s[l]] == 0:
                        del char_count_map[s[l]]
                    l+=1
            r+=1
        return max_len if max_len != float('-inf') else 0
                