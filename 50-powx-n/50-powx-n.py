class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            # base case
            if n == 0: return 1
            if x == 0: return 0
            r = helper(x,n//2)
            r = r*r
            return r * x if n % 2 == 1 else r
        res = helper(x,abs(n))
        return res if n >= 0 else 1/res