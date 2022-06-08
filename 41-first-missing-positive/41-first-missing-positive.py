class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1st iteration to convert -ve into 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # 2nd iteration to mark the nums[nums[i]-1] as -ve to tell nums[i] does exists
        for i in range(len(nums)):
            value = abs(nums[i])
            if 1 <= value <= len(nums):
                if nums[value-1] > 0:
                    nums[value-1]  = -1 * nums[value-1]
                elif nums[value-1] == 0:
                    nums[value-1] = -1*(len(nums)+1)
        
        for i in range(1,len(nums)+1):
            if nums[i-1] >= 0:
                return i
        return len(nums)+1
            
            