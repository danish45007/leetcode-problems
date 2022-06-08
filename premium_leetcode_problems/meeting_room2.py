'''

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

'''

from typing import (
    List,
)
from lintcode import (
    Interval,
)

import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key=lambda t: t.end)
        min_heap = [] #[end]
        overlapping_meetings = 0
        res = 0
        for interval in intervals:
            start,end = interval.start,interval.end
            overlapping_meetings += 1
            # new meeting is not overlapping
            while min_heap and min_heap[0] <= start:
                _end = heapq.heappop(min_heap)
                overlapping_meetings -= 1
            heapq.heappush(min_heap,end)
            res = max(res,overlapping_meetings)
        return res
    
    
        # start_interval = sorted([i.start for i in intervals]) 
        # end_interval = sorted([i.end for i in intervals])
        # count = 0
        # s,e = 0,0
        # res = 0
        # while s < len(intervals):
        #     if start_interval[s] < end_interval[e]:
        #         s+=1
        #         count +=1
        #     else:
        #         e +=1
        #         count-=1
        #     res = max(res,count)
        # return res


