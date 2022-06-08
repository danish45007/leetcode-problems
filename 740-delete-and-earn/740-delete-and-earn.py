class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev_earn,prev_to_prev_earn = 0,0
        # sort and set
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        
        for i in range(len(nums)):
            earn = nums[i]*count[nums[i]]
            # check if a valid adj
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp_prev_earn = prev_earn
                prev_earn = max(earn + prev_to_prev_earn,prev_earn)
                prev_to_prev_earn = temp_prev_earn
            else:
                temp_prev_earn = prev_earn
                prev_earn = earn + prev_earn
                prev_to_prev_earn = temp_prev_earn
        return prev_earn
                