class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res= 0
        _sum = 0
        _map = {0:1}
        for num in nums:
            _sum += num
            delta = _sum - k
            res += _map.get(delta,0)
            _map[_sum] = 1 + _map.get(_sum,0)
        return res
            