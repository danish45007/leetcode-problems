class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,interval in enumerate(intervals):
            # if new interval not overlapping with the first interval
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            # non overlapping with after first
            elif interval[1] < newInterval[0]:
                res.append(interval)
            # overlapping
            else:
                newInterval = [min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)
        return res
                
                
                
                
                