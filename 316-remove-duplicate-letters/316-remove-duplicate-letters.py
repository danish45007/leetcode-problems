class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen_char = set()
        freq_count = {}
        for char in s:
            freq_count[char] = 1 + freq_count.get(char,0)
        
        stack = []
        
        for char in s:
            freq_count[char] -=1
            if char in seen_char:
                continue
            # check if the top of the stack has bigger char and freq of top is greater than 0
            # pop from stack and remove from seen
            while stack and ord(stack[-1])-ord(char) > 0 and freq_count[stack[-1]] > 0:
                c = stack.pop()
                seen_char.remove(c)
            stack.append(char)
            seen_char.add(char)
        return ''.join(stack)