class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set(nums)
        for i in range(0,len(nums)):
            if i in hash_set:
                continue
            else:
                return i
        return len(nums)