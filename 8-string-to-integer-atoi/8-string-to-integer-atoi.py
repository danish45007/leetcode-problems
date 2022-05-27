class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        max_int = pow(2,31)-1
        min_int = -pow(2,31)
        signed = 1
        valid_num = {str(i) for i in range(10)}
        # white space (igoring whitespaces)
        while i < len(s) and s[i] == " ":
            i +=1
        
        # taking care if sign
        if i < len(s) and s[i] == '-':
            i +=1
            signed = -1
        elif i < len(s) and s[i] == '+':
            i +=1
        
        while i < len(s) and s[i] in valid_num:
            res = res*10 + ord(s[i]) - ord('0')
            i +=1
        
        res = res*signed
        if res > max_int:
            return max_int
        elif res < min_int:
            return min_int
        else:
            return res
        
    
        
        
        
        
                