class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        min_heap = [] # [end,no_of_pes]
        curr_pes = 0
        for t in trips:
            pes,start,end = t
            curr_pes += pes
            while min_heap and min_heap[0][0] <= start:
                last_end,last_pes = heapq.heappop(min_heap)
                curr_pes -= last_pes
            if(curr_pes > capacity):
                return False
            heapq.heappush(min_heap,[end,pes])

        return True
                
                
        