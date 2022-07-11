class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        moves = 0
        for num in nums:
            moves += num-min_num
        return moves