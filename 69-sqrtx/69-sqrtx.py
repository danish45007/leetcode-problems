class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        res = -1
        if x == 0 or x == 1:
            return x
        while start <= end:
            mid = start + (end-start) // 2
            if(mid*mid == x):
                return int(mid)
            if(mid*mid <= x):
                start = mid + 1
                res = mid 
            if(mid*mid >= x):
                end = mid - 1
        return res
                