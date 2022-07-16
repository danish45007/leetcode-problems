class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = [0]*len(nums)
        right_min = [0]*len(nums)
        
        curr_max,curr_min = nums[0],nums[-1]
        for i in range(len(nums)):
            curr_max = max(curr_max,nums[i])
            left_max[i] = curr_max
        for j in range(len(nums)-1,-1,-1):
            curr_min = min(curr_min,nums[j])
            right_min[j] = curr_min
        
        for k in range(len(nums)-1):
            if left_max[k] <= right_min[k+1]:
                return k+1