class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # l,r = 0,len(x)-1
        # while l < r:
        #     if x[l] != x[r]:
        #         return False
        #     l +=1
        #     r -=1
        # return True
        
        # follow up without converting into string
        if x < 0: return False
        div = 1
        while x >= div*10:
            div = div*10

        while x:
            right_digit = x % 10
            left_digit = x // div
            if right_digit != left_digit: return False
            
            # moving left and right
            # in this case trimming the curr left and right to update the new left and right
            
            # trimming left
            x = x % div
            # trimming left
            x = x // 10
            # updating div as 2 digits are removed
            div = div / 100
        return True
        
        