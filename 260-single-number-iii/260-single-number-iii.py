class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1,len(nums)):
            xor ^= nums[i]
        mask = (xor & (xor-1))^xor
        num1 = 0
        for n in nums:
            if mask&n == 0:
                num1 = n^num1
        return [num1,xor^num1]