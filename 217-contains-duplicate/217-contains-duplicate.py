class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _map = {}
        for num in nums:
            _map[num] = 1 + _map.get(num,0)
        for key in _map:
            if(_map[key] >= 2):
                return True
        return False