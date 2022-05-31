class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap,-1*int(num))
        while k > 0:
            n = heapq.heappop(max_heap)
            k -=1
        return str(-1*n)
            