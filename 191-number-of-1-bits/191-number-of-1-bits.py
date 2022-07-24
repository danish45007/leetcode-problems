class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # check if one
            count += n%2
            # processing the remaining integer by right shifting 1 bit
            n = n >> 1
        return count