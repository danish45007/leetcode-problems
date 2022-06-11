class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = ''
        # going from left to right and taking left parantheses greedly
        # valid condition to add right would if l_count > right_count
        l_count = r_count = 0
        for char in s:
            if char == '(':
                stack.append(char)
                l_count +=1
            elif char == ')':
                if l_count > r_count:
                    stack.append(char)
                    r_count +=1
            else:
                stack.append(char)
        
        # valid parantheses was able remove extra right parantheses
        if l_count == r_count:
            return ''.join(stack)
        # in case where left count exceeded the right count now need to perform an iteration from right to left
        # and valid condition would if l_count < r_count
        else:
            for char in reversed(stack):
                if char == '(':
                    if r_count < l_count:
                        l_count -=1
                        continue
                    else:
                        result += char
                elif char == ')':
                    result += char
                else:
                    result += char
            return result[::-1]
                        
            
            
