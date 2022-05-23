class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using linear time and space
        _map = {}
        for num in nums:
            _map[num] = 1 + _map.get(num,0)
        for n,count in _map.items():
            if count > len(nums) // 2:
                return n