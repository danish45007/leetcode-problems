class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = deque()
        for char in s:
            if char == ')':
                while stack[-1] != '(':
                    queue.append(stack.pop())
                # remove the opening bracket
                stack.pop()
                # add the element back into stack from queue
                while queue:
                    stack.append(queue.popleft())
            else:
                stack.append(char)
        return ''.join(stack)