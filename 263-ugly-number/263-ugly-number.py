class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        prime_factors = [2,3,5]
        for prime_factor in prime_factors:
            while n % prime_factor == 0:
                n = n // prime_factor
        return n == 1