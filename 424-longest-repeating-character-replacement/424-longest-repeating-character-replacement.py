class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_sub_string_length = 0
        char_count = {}
        left,right = 0,0
        while right < len(s):
            char_count[s[right]] = 1 + char_count.get(s[right],0)
            while (right-left+1) - max(char_count.values()) > k:
                char_count[s[left]] -=1
                left +=1
            max_sub_string_length = max(max_sub_string_length,(right-left+1))
            right +=1
        return max_sub_string_length