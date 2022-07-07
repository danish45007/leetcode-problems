class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            # seen nums[r] for the first time
            if nums[r] != nums[r-1]:
                # placing the unique element in the right spot
                nums[l] = nums[r]
                # going for next right spot
                l+=1
        return l
                
        