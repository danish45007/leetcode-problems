class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        n = len(nums)
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for i in range(n):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack()
                perm.pop()
        backtrack()
        return result


        