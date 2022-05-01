class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_end = intervals[0][1]
        count = 0
        for start,end in intervals[1:]:
            # non overlapping
            if start >= prev_end:
                # update the prev to new end
                prev_end = end
            # overlapping
            else:
                count +=1
                # update prev_end with the min value so the scope for future overlapping reduces
                prev_end = min(prev_end,end)
        return count
                
                
