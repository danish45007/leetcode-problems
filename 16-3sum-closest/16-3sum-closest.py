class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = 0
        for i,num in enumerate(nums):
            left,right = i+1,len(nums)-1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == target:
                    return target
                elif diff > abs(three_sum-target):
                    diff = abs(three_sum-target)
                    res = three_sum
                    
                elif three_sum > target:
                    right = right-1
                elif three_sum < target:
                    left = left + 1
        return res