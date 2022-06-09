class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = 1 + char_count.get(char,0)
        res = ''
        for char in order:
            if char in char_count:
                res += str(char*char_count[char])
                del char_count[char]
        for char,freq in char_count.items():
            res += str(freq*char)
        return res