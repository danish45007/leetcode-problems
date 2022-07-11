class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total_sum,l = 0,0
        res = float('inf')
        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target:
                res = min(res,r-l+1)
                total_sum -= nums[l]
                l +=1
        return res if res != float('inf') else 0
                