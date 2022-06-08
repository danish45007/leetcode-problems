class StockPrice:

    def __init__(self):
        self.time_price_map = {} # {time_stamp: price}
        self.curr_timestamp = -1
        self.max_price = []
        self.min_price = []

    def update(self, timestamp: int, price: int) -> None:
        self.time_price_map[timestamp] = price
        self.curr_timestamp = max(self.curr_timestamp,timestamp)
        heapq.heappush(self.max_price,(-price,timestamp))
        heapq.heappush(self.min_price,(price,timestamp))
        

    def current(self) -> int:
        return self.time_price_map[self.curr_timestamp]

    def maximum(self) -> int:
        curr_price,timestamp = heapq.heappop(self.max_price)
        while -1*curr_price != self.time_price_map[timestamp]:
            curr_price,timestamp = heapq.heappop(self.max_price)
        heapq.heappush(self.max_price,(curr_price,timestamp))
        return -1*curr_price
        
        

    def minimum(self) -> int:
        curr_price,timestamp = heapq.heappop(self.min_price)
        while curr_price != self.time_price_map[timestamp]:
            curr_price,timestamp = heapq.heappop(self.min_price)
        heapq.heappush(self.min_price,(curr_price,timestamp))
        return curr_price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()