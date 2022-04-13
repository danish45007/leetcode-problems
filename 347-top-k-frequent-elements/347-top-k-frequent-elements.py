class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = {}
        res = []
        for num in nums:
            _map[num] = 1 + _map.get(num,0)
        heap = [(val,key) for key,val in _map.items()]
        for val,key in (sorted(heap,reverse=True)[0:k]):
            res.append(key)
        return res
        
        
            