class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq_count = {}
        for num in nums:
            freq_count[num] = 1 + freq_count.get(num,0)
        pair,left = 0,0
        for num in freq_count:
            pair += freq_count[num] // 2
            left += freq_count[num] % 2
        return [pair,left]