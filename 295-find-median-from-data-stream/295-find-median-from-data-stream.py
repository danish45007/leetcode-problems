class MedianFinder:

    def __init__(self):
        '''
            small_heap will have to maintain elements in it smaller than large heap
            and the size has to be approx. equal abs(len(small)-len(large)) > 1
        '''
        # large heap min heap
        self.large_heap = [] 
        # small heap max heap
        self.small_heap = []

    def addNum(self, num: int) -> None:
        # initally adding num into small heap (max_heap)
        heapq.heappush(self.small_heap,-num)
        
        # maintain elements in smaller heap less than elements in larger heap
        # its a one way operation as initally we are adding elements into small_heap only
        if(self.small_heap and self.large_heap and -self.small_heap[0] > self.large_heap[0]):
            # move element from small into large heap
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)
        
        # maintain the approx. size of both the heaps
        if(len(self.small_heap)-len(self.large_heap) > 1):
            # move element from small to large
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap,val)
        if(len(self.large_heap)-len(self.small_heap) > 1):
            # move element from large to small
            val = -heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap,val)
            

    def findMedian(self) -> float:
        # in case of odd number of elements
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        
        if len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]
        
        # in case of even number of elements
        return (-1*self.small_heap[0] + self.large_heap[0])/2
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()