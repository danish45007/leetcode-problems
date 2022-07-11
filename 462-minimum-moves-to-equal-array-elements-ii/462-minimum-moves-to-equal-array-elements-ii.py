class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        pivot = len(nums)//2
        center_element = nums[pivot]
        moves = 0
        for num in nums:
            moves += abs(center_element-num)
        return moves