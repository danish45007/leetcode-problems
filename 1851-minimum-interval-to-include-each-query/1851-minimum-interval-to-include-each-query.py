class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i:i[0])
        result = {}
        heap = []
        i = 0
        for q in sorted(queries):
            # add the intervals into heap for the given query
            while i < len(intervals) and intervals[i][0] <= q:
                interval_start,interval_end = intervals[i] 
                heapq.heappush(heap,(interval_end-interval_start+1,interval_end))
                i+=1
            # pop out the invalid intervals from the heap againstthe given query
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            # after the while loop ends we will at all potential intervals that satisfy the query
            # take the min if heap in not null otherwise -1
            min_val = heap[0][0] if heap else -1
            result[q] = min_val
        return [result[q] for q in queries]
        