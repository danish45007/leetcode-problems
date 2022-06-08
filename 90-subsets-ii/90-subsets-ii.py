class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def back_track(i,subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            # include nums[i] into subset
            subset.append(nums[i])
            # call backtrack
            back_track(i+1,subset)

            # don't include nums[i] into subset
            subset.pop()
            # check for the duplicate element in subset
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i +=1
            back_track(i+1,subset)
        back_track(0,[])
        return result
                    
            