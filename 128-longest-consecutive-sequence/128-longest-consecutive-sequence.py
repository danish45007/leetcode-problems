class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, res = set(nums), 0
        print(s)
        for i, n in enumerate(nums):
            
            if n-1 not in s:
                length = 0
                while n+length in s:
                    s.remove(n+length)
                    length += 1
                res = max(res, length)
        return res
                
            
        
        
                
