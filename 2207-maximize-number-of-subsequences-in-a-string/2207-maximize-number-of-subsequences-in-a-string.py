class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        pre_append_string,post_append_string = pattern[0] + text, text + pattern[1]
        def count_subsequnece(s):
            count,res = 0,0
            for i in range(len(s)):
                if s[i] == pattern[0]:
                    count +=1
                elif s[i] == pattern[1]:
                    res += count
            if(pattern[0] == pattern[1]):
                res = (count * (count - 1)) // 2
            return res
        return max(count_subsequnece(pre_append_string),count_subsequnece(post_append_string))
            