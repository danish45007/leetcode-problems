class Solution:
    def calculate(self, s: str) -> int:
        # removing all the whitespaces
        s=s.replace(" ",'')
        valid_nums = {str(i) for i in range(10)}
        valid_opertaions = {'+','-','*','/'}
        stack = []
        prev_operator = '+'
        curr_num = 0
        for i in range(len(s)):
            char = s[i]
            if char in valid_nums:
                curr_num = curr_num*10 + int(char)
            if char in valid_opertaions or i == len(s) - 1:
                if prev_operator == '+':
                    stack.append(curr_num)
                elif prev_operator == '-':
                    stack.append(-curr_num)
                elif prev_operator == '*':
                    stack[-1] = stack[-1] * curr_num
                elif prev_operator == '/':
                    stack[-1] = int(stack[-1]/curr_num)
                prev_operator = char
                curr_num = 0
        return sum(stack)
                