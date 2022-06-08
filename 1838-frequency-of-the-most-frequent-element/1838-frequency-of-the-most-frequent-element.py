class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l,r = 0,0
        max_window_size = 0
        while r < len(nums):
            total += nums[r]
            while nums[r]*(r-l+1) > (total+k):
                total -= nums[l]
                l += 1
            max_window_size = max(max_window_size,(r-l+1))
            r +=1
            
            
        return max_window_size