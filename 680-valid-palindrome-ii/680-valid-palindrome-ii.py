class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid_palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True
        l_pointer = 0
        r_pointer = len(s)-1
        while l_pointer < r_pointer:
            if s[l_pointer] == s[r_pointer]:
                l_pointer +=1
                r_pointer -=1
            else:
                if is_valid_palindrome(l_pointer+1,r_pointer):
                    return True
                if is_valid_palindrome(l_pointer,r_pointer-1):
                     return True
                return False
            
        return True