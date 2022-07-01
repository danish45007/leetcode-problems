class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            # assuming num[i] to be the max element in nums array and w.r.t trying to minimize the range diff. by calculating 
            # the min value as close as to the num[i] + k (assumed max) 
            min_val = min(nums[0]+k,nums[i+1]-k)
            max_val = max(nums[i]+k,nums[-1]-k)
            res = min(res,max_val-min_val)
        return res