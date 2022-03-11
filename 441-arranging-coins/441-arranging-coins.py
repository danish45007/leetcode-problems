class Solution:
    def arrangeCoins(self, n: int) -> int:
        # log(n) solution
        left = 1
        right = n
        max_row = 0
        while left <= right:
            mid = (left + right) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                max_row = max(mid,max_row)
        return max_row
                
        