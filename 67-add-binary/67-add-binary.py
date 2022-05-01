class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a,b = a[::-1],b[::-1]
        carry = 0
        # a and b can of different size
        for i in range(max(len(a),len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else "0"
            digit_b = ord(b[i]) - ord("0") if i < len(b) else "0"
            total = int(digit_a) + int(digit_b) + carry
            char = str(total%2)
            res = res + char
            carry = total // 2
        res = res[::-1]    
        if carry:
            res = "1" + res
        return res