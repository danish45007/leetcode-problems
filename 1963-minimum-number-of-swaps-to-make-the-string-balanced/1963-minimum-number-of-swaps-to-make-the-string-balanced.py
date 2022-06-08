class Solution:
    def minSwaps(self, s: str) -> int:
        max_close = 0
        extra_closing = 0
        for c in s:
            if c == ']':
                extra_closing +=1
            else:
                extra_closing -=1
            
            max_close  = max(max_close,extra_closing)
        return (max_close + 1)//2 