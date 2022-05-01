class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        while k > 0:
            res = heapq.heappop(heap)
            k -=1
        return -res
            
                