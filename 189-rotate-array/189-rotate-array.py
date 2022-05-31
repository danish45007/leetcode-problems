class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using extra memory
        res = [0]*len(nums)
        for i in range(len(nums)):
            idx = (i+k)%len(nums)
            res[idx] = nums[i]
        nums[:] = res
        
        # without using extra memory
        nums = list(reversed(nums))
        kth_part = nums[:k+1]
        non_kth_part = nums[k+1:]
        nums = list(reversed(kth_part)) + list(reversed(non_kth_part))
        