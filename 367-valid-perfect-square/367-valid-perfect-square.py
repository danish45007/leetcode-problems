class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # brute force O(sqrt(n))
        for i in range(1,num+1):
            if i*i == num:
                return True
            # return False immediately
            if i*i > num:
                return False
        # binary search logn solution
        # start = 1
        # end = num
        # while start <= end:
        #     mid = (start + end) // 2
        #     if mid*mid == num:
        #         return True
        #     elif mid*mid > num:
        #         end = mid - 1
        #     elif mid*mid < num:
        #         start = mid + 1
        # return False