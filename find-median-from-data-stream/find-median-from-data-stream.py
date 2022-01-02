class MedianFinder(object):

    def __init__(self):
        """
            initialize two heaps
            small heap -> max heap -> contain smaller elements
            large heap -> min heap -> contains larger elements
        """
        self.small_heap = []  # max heap
        self.large_heap = []  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # add nums into small heap
        #hack to make max heap
        heapq.heappush(self.small_heap,-1*num)
            
        # largest element in small heap greater than smallest element in large_heap
        # pop from small heap and push into large heap
        if(self.small_heap and self.large_heap 
           and (-1 * self.small_heap[0]) > self.large_heap[0]):
            small_heap_val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, small_heap_val)
            
        # small heap size greater than large heap
        if(len(self.small_heap) > len(self.large_heap)+1):
            small_heap_val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, small_heap_val)
        
        # small heap size smaller than large heap
        if(len(self.large_heap) > len(self.small_heap)+1):
            large_heap_val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * large_heap_val)
        
            
            

    def findMedian(self):
        """
        :rtype: float
        """
        # odd number of element case
        if (len(self.small_heap) > len(self.large_heap)):
            return -1 * self.small_heap[0]
        
        if (len(self.large_heap) > len(self.small_heap)):
            return self.large_heap[0]
        
        # even number of element case
        if len(self.large_heap) == len(self.small_heap):
            return float((-1 * self.small_heap[0]) + self.large_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()