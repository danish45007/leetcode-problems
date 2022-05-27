class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)
        right_index = len(nums) - 1
        for left_index,left in enumerate(nums):
            while left + nums[right_index] > target and left_index <= right_index:
                right_index -= 1
            
            if left_index <= right_index:
                res +=  pow(2, right_index - left_index, mod)  
        return res%mod