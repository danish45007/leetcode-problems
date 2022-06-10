class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not len(s):
            return 0
        l_count,r_count = 0,0
        max_size = 0
        def check_longest_from_left_to_right(start,end):
            nonlocal max_size
            left_count,right_count = 0,0
            while start <= end:
                if s[start] == '(':
                    left_count +=1
                else:
                    right_count += 1
                
                if left_count == right_count:
                    max_size  = max(max_size,left_count+right_count)
                elif right_count > left_count:
                    left_count,right_count = 0,0
                start +=1
            return max_size
        
        def check_longest_from_right_to_left(start,end):
            nonlocal max_size
            left_count,right_count = 0,0
            while start >= end:
                if s[start] == '(':
                    left_count +=1
                else:
                    right_count += 1
                
                if left_count == right_count:
                    max_size  = max(max_size,left_count+right_count)
                elif left_count > right_count:
                    left_count,right_count = 0,0
                start -=1
            return max_size
        
        max_from_left = (check_longest_from_left_to_right(0,len(s)-1))
        max_from_right = (check_longest_from_right_to_left(len(s)-1,0))
        return max(max_from_left,max_from_right)
        
            
            
                