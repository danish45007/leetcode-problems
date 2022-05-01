class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr_len = 0
            while nums[i] != -1:
                temp = i
                i = nums[i]
                nums[temp] = -1
                curr_len +=1
            res = max(res,curr_len)
        return res