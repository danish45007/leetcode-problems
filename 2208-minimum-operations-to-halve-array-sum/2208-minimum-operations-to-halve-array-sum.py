class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = 0
        count = 0
        heap = []
        for num in nums:
            total_sum +=num
            heapq.heappush(heap,-1*num)
        target = total_sum / 2
        while total_sum > target:
            top = -1*heapq.heappop(heap)
            total_sum -= top/2
            heapq.heappush(heap,-1*top/2)
            count +=1
        return count
            
            