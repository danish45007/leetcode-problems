class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones,twoes = 0,0
        for num in nums:
            # xor with num and compliment with twoes
            ones = (num^ones) & (~twoes)
            # xor with num and compliment with ones
            twoes  = (num^twoes) & (~ones)
        return ones