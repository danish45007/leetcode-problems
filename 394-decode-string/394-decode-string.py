class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            # add char in stack until not reached the closing bracket
            if char != "]":
                stack.append(char)
            # reached the closing bracket
            if char == "]":
                substring = ""
                # start poping and adding into substring until not reached the opening bracket
                while stack[-1] != "[":
                    # adding char in substring in order
                    substring = stack.pop() + substring
                # extra pop required to remove the opening bracket
                stack.pop()
                k = "" # interger value
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substring)
        return "".join(stack)
                    
                
                
            