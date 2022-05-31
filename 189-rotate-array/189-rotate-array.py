class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        for i in range(len(nums)):
            idx = (i+k)%len(nums)
            res[idx] = nums[i]
        nums[:] = res