class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        _map = {}
        count = 0
        for n in nums:
            _map[n] = 1 + _map.get(n,0)
        for key,val in _map.items():
            if k == 0 and _map[key] > 1:
                count +=1
            elif(k > 0 and k+key in _map):
                count +=1
        return count
                