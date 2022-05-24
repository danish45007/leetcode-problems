class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start <= end:
            mid = (start + end) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                end = mid - 1
            elif mid*mid < num:
                start = mid + 1
        return False