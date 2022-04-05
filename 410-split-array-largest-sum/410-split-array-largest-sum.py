class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start = max(nums)
        end = sum(nums)
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if(self.is_valid_sub_array_sum(nums,m,mid)):
                res = mid
                end = mid -1
            else:
                start = mid + 1
        return res
    def is_valid_sub_array_sum(self,nums,m,curr_max):
        sub = 1
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if(_sum > curr_max):
                sub +=1
                _sum = nums[i]
        if(sub > m):
            return False
        else:
            return True