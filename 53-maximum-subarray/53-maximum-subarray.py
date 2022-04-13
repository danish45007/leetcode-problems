class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_array_sum = [0] * len(nums)
        sub_array_sum[0] = nums[0]
        for i in range(1,len(nums)):
            sub_array_sum[i] = max(nums[i],sub_array_sum[i-1]+nums[i])
        return max(sub_array_sum)
        