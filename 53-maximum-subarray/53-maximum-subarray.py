class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_string_sum = [0]*len(nums)
        sub_string_sum[0] = nums[0]
        for i in range(1,len(nums)):
            sub_string_sum[i] = max(nums[i],nums[i] + sub_string_sum[i-1])
        return max(sub_string_sum)
        