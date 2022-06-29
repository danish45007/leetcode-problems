class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_valid_prime(num):
            if num < 2:
                return False
            for i in range(2,int(sqrt(num)) + 1):
                if num%i == 0:
                    return False
            return True
        
        def is_valid_palindrome(num):
            num_str = str(num)
            l,r = 0,len(num_str)-1
            while l < r:
                if num_str[l] != num_str[r]:
                    return False
                else:
                    l +=1
                    r -=1
            return True
        
        
        def get_next_palindrome(num):
            if is_valid_prime(num+1) and is_valid_palindrome(num+1):
                return num+1
            num_str = list(str(num))
            mid = len(num_str) // 2
            char_at_mid = num_str[mid]
            new_mid_val = int(char_at_mid) + 1
            num_str[mid] = new_mid_val
            # transforming the right of mid
            j = 1
            for i in range(mid-1,-1,-1):
                num_str[mid+j] = num_str[i]
                j+=1
            res_str = ''.join([str(i) for i in num_str])
            return int(res_str)
            
            
        
        while True:
            str_num = str(n)
            if n > 11 and len(str_num) % 2 == 0:
                n = 10**len(str_num)
            if is_valid_prime(n) and is_valid_palindrome(n):
                return n
            mid = len(str_num) // 2
            char_at_mid = str_num[mid]
            if char_at_mid in ['9'] or n <= 11:
                n +=1
            else:
                # check only for next possible palindrome number
                next_palindrome = get_next_palindrome(n)
                n = next_palindrome
            

        