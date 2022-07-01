class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # monotonically inc order
        for char in num:
            while k > 0 and stack and ord(stack[-1]) > ord(char):
                k -=1
                stack.pop()
            stack.append(char)
        # stack was already in mono inc order
        stack = stack[:len(stack)-k] # remove k digits from lsb
        # removing the leading zeros
        res = ''.join(stack)
        return str(int(res)) if res else "0"