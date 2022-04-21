class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # when the new interval is non overlapping and comes before the curr interval
            if newInterval[1] < intervals[i][0]:
                # append the new interval at start of curr interval
                res.append(newInterval)
                return res + intervals[i:]
            # when the new interval is non overlapping but comes after curr interval
            elif newInterval[0] > intervals[i][1]:
                # will all the intervals before the new interval into result
                # as new interval can overlap with next interval so we not add the new interval before check the overlapping case
                res.append(intervals[i])
            # when curr and new interval overlaps
            else:
                # once new interval and curr interval overlaps the new interval will have the start as min(curr_start,new_start)
                # and end as max(curr_end,new_end)
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
            
        # once iterated over interval add the new interval into result
        res.append(newInterval)
        return res
                
                