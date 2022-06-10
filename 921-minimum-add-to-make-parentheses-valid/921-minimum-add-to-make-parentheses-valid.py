class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = right_count = min_add = 0
        for char in s:
            # taking left parentheses gredly
            if char == "(":
                left_count +=1
            else:
                # inc. the right_count if the curr state if valid parentheses(l > r)
                if left_count > right_count:
                    right_count +=1
                else:
                    min_add +=1
        
        min_add += left_count - right_count
        return min_add
                    
                