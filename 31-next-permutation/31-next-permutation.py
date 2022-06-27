class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        
        # finding the pivot
        pivot = length - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -=1
        
        # if not found return the reverse
        if pivot == -1:
            return nums.reverse()
        
        # replacing the pivot element with least greater element
        for i in range(length-1,pivot,-1):
            if nums[pivot] < nums[i]:
                nums[pivot],nums[i] = nums[i],nums[pivot]
                break
        nums[pivot+1:] = reversed(nums[pivot+1:])
        