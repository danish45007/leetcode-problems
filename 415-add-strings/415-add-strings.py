class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1)-1
        p2 = len(num2)-1
        carry = 0
        res = []
        while p1 >= 0 or p2 >= 0 or carry:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            _sum = n1 + n2 + carry
            result = _sum % 10
            carry = _sum // 10
            res.append(str(result))
            p1 -= 1
            p2 -= 1
        return ''.join(reversed(res))