class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = 0
        i,j = 0,0
        min_size = float('inf')
        while j < len(nums):
            _sum += nums[j]
            while _sum >= target:
                min_size = min(min_size,j-i+1)
                _sum -= nums[i]
                i+=1
            j+=1
        return min_size if min_size != float('inf') else 0