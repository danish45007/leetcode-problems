class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p1,p2 in points:
            dist = (p1**2 + p2**2)**0.5
            # min heap
            heapq.heappush(heap,(dist,[p1,p2]))
        while k > 0:
            d,point = heapq.heappop(heap)
            res.append(point)
            k -=1
        return res