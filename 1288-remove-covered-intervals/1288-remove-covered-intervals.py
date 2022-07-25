class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        prev_ending = float('-inf')
        res = 0
        for start,end in intervals:
            if end > prev_ending:
                res+=1
                prev_ending = end
        return res