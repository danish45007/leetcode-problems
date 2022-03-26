class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _map = {}
        for i in range(len(nums)):
            curr = nums[i]
            if(curr in _map and abs(i-_map.get(curr)) <= k):
                return True
            else:
                _map[curr] = i
        return False