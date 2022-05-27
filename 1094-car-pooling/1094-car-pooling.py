class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n)
        # total passengers from all start to end
        change_in_passengers = [0]*1001
        for t in trips:
            pessengers,start,end = t
            # pessengers will be added at start index
            change_in_passengers[start] += pessengers
            # pessengers will be removed at end index
            change_in_passengers[end] -= pessengers
        
        # checking pessengers for the each index
        curr_pessengers = 0
        for i in range(1001):
            curr_pessengers += change_in_passengers[i]
            if curr_pessengers > capacity:
                return False
        return True
            
        
    
        # O(nlogn)
#         trips.sort(key=lambda t: t[1])
#         min_heap = [] # [end,no_of_pes]
#         curr_pes = 0
#         for t in trips:
#             pes,start,end = t
#             curr_pes += pes
#             while min_heap and min_heap[0][0] <= start:
#                 last_end,last_pes = heapq.heappop(min_heap)
#                 curr_pes -= last_pes
#             if(curr_pes > capacity):
#                 return False
#             heapq.heappush(min_heap,[end,pes])

#         return True
                
                
        