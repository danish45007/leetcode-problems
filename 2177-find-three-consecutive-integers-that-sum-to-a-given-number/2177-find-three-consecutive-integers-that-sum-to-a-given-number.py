class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # compresence
        if num % 3 == 0:
            n = num // 3
            return [n-1, n, n+1]
        return []