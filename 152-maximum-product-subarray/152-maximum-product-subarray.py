class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max,curr_min = 1,1
        res = max(nums)
        for n in nums:
            tem_max=curr_max
            curr_max = max(curr_max*n,curr_min*n,n)
            curr_min = min(tem_max*n,curr_min*n,n)
            res = max(res,curr_max)
        return res
            
