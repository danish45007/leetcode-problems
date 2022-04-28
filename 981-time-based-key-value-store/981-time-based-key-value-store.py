class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self._map.get(key,[])
        if len(values) > 0:
            # apply binary search to find timestamp or small neareast
            l,r = 0,len(values)-1
            while l <= r:
                mid = (l+r) // 2
                if values[mid][1] == timestamp:
                    return values[mid][0]
                if values[mid][1] < timestamp:
                    res = values[mid][0]
                    l = mid + 1
                if values[mid][1] > timestamp:
                    r = mid - 1 
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)