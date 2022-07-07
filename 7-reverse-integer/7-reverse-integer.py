class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            # check intger overflow
            if ((res > MAX_INT//10) or (res == MAX_INT//10 and digit >= MAX_INT%10)):
                return 0
            if ((res < MIN_INT//10) or (res == MIN_INT//10 and digit <= MIN_INT%10)):
                return 0
            res = (res*10)+digit
        return res