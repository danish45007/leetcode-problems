class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        # step1 is to find out the index where the sum is +ve from the right to left
        positive_idx = len(satisfaction)-1
        total = 0
        for i in range(len(satisfaction)-1,-1,-1):
            total += satisfaction[i]
            if total < 0:
                break 
            positive_idx = i
        
        # calucalte the like-for the positive range only (this will give max)
        time = 1
        res = 0
        for i in range(positive_idx,len(satisfaction)):
            res += time*satisfaction[i]
            time +=1
        return res if res > 0 else 0