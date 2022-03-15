class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums[i]
            perms = self.permute(nums[:i]+nums[i+1:])
            for perm in perms:
                perm.append(n)
            result.extend(perms)
        return result


        