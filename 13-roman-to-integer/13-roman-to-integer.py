class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        prev,running_total = 0,0
        for i in range(len(s)-1,-1,-1):
            curr = romans[s[i]]
            if prev > curr:
                running_total -= curr
            else:
                running_total += curr
            prev = curr
        return running_total