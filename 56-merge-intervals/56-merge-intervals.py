class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on the start value
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for start,end in intervals[1:]:
            last_end = res[-1][1]
            # in case of overlapping
            if last_end >= start:
                # updating the end of the output as overlapping
                res[-1][1] = max(last_end,end)
            # if not overlapping
            else:
                res.append([start,end])
        return res
            