class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sub_array_sum = [0]*len(nums)
        # sub_array_sum[0] = nums[0]
        # for i in range(1,len(nums)):
        #     # out of 2 decisions taking the max of two
        #     # d1 adding the curr number to prev sum
        #     # d2 starting from curr number
        #     sub_array_sum[i] = max(sub_array_sum[i-1]+nums[i],nums[i])
        # return max(sub_array_sum)
        
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(curr_sum,max_sum)
        return max_sum
            
    
    
        