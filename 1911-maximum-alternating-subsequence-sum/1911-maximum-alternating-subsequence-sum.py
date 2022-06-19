class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {} #{(index,is_even): max_sum}
        def dfs(i,is_even):
            if i == len(nums):
                return 0
            if (i,is_even) in dp:
                return dp[(i,is_even)]
            curr_total = nums[i] if is_even else -nums[i]
            dp[(i,is_even)] = max(curr_total+dfs(i+1,not is_even),dfs(i+1,is_even))
            return dp[(i,is_even)]
        
        return dfs(0,True)