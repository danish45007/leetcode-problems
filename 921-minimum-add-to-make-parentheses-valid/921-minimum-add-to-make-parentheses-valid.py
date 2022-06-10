class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = right_count = min_add = 0
        for char in s:
            # taking left parentheses greedily
            if char == "(":
                left_count +=1
            else:
                # inc. the right_count if the curr state if valid parentheses(l > r)
                if left_count > right_count:
                    right_count +=1
                # under the invalid case inc. the add pointer indicating we can can more left parentheses
                else:
                    min_add +=1
        
        # at end remove the extra left which was done greedily
        min_add += left_count - right_count
        return min_add
                    
                