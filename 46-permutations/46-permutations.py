class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            first_element = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(first_element)
            result.extend(perms)
            nums.append(first_element)
        return result
                


        