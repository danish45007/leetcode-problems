class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        _sum = 0
        sub_arr = 0
        if(k < nums[0]):
            return 0
        while j < len(nums):
            _sum += nums[j]
            
            if(_sum < k):
                j += 1
            elif(_sum == k):
                sub_arr = sub_arr + 1
                j += 1
            else:
                while _sum > k:
                    _sum = _sum - nums[i]
                    i +=1
                    if(_sum == k):
                        sub_arr = sub_arr + 1
                j +=1
        return sub_arr