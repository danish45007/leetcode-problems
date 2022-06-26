class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for char in range(1,n+1):
            if char % 3 == 0 and char % 5 == 0:
                res.append("FizzBuzz")
            elif char % 5 == 0:
                res.append("Buzz")
            elif char % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(char))
        return res
                