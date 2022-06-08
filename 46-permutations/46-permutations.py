class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            first_pop = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(first_pop)
            res.extend(perms)
            nums.append(first_pop)
        return res
                
        
        