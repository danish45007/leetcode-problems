class Solution:
    def minDeletions(self, s: str) -> int:
        min_deletion = 0
        _map = {}
        _set = set()
        for char in s:
            _map[char] = 1 + _map.get(char,0)
        for key,val in _map.items():
            while val > 0 and val in _set:
                val -=1
                min_deletion +=1
            _set.add(val)
        return min_deletion