class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in _map:
                return [_map[diff],i]
            _map[num] = i
        return

            