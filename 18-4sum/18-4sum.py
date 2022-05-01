class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort array,this way we can safely ignore repeating values
        # because after sort,same values come one after one
        nums.sort()
        result = []
		
        for i in range(len(nums)):
			# if repeating value,ignore the value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # solve 3sum problem with nums[i]
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # solve 2sum problem with nums[i]+nums[j]
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    # if total sum of 4 numbers equal to target,append to result list
                    tot = nums[i] + nums[j] + nums[l] + nums[r]
                    if tot == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    # if total is less than target value,we need a bigger total
                    # move p pointer forward to make bigger total
                    elif tot < target:
                        l += 1
                    # if total is bigger than target value,we need a smaller total
                    # move q pointer backward to make small total
                    else:
                        r -= 1

        return result