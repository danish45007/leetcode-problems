class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_mapping = {')':'(','}':'{',']':'['}
        for char in s:
            if char in close_to_open_mapping:
                if stack and stack[-1] == close_to_open_mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        