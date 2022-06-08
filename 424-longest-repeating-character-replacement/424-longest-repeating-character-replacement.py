class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_sub_string = 0
        l,r = 0,0
        char_count = {}
        while r < len(s):
            char_count[s[r]] = 1 + char_count.get(s[r],0)
            while r-l+1 - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l+=1
            max_sub_string = max(max_sub_string,r-l+1)
            r+=1
        return max_sub_string