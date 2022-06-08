class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        res = []
        for num in arr:
            heapq.heappush(min_heap,[abs(num-x),num])
        
        while k > 0:
            key,num = heapq.heappop(min_heap)
            res.append(num)
            k -= 1
        res.sort()
        return res