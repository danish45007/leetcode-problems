class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max,curr_min = 1,1
        for n in nums:
            tem_max = n*curr_max
            curr_max = max(n*curr_max,n*curr_min,n)
            curr_min = min(tem_max,n*curr_min,n)
            res = max(res,curr_max,curr_min)
        return res
            
            
