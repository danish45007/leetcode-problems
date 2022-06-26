class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     curr_len = 0
        #     while nums[i] != -1:
        #         temp = i
        #         i = nums[i]
        #         nums[temp] = -1
        #         curr_len +=1
        #     res = max(res,curr_len)
        # return res
        longest = 0
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                length = 0
                idx = nums[i]
                while idx != nums[i] or length == 0:
                    length +=1
                    visited.add(idx)
                    idx = nums[idx]
                longest = max(longest,length)
        return longest
                