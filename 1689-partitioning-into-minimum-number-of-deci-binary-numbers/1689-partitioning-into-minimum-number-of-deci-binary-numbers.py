class Solution:
    def minPartitions(self, n: str) -> int:
        max_value = -1
        for i in n:
            a = int(i)
            if a > max_value:
                max_value = a
                
        return max_value