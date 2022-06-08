class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i,num in enumerate(nums):
            right_sum = total - num - left_sum
            if left_sum == right_sum:
                return i
            left_sum += num
            
        return -1