class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_map = defaultdict(int)
        count = 0
        for t in time:
            if t%60 == 0:
                count += remainder_map[0]
            else:   
                rem_needed = 60-(t%60)
                if rem_needed in remainder_map:
                    count +=remainder_map[rem_needed]
            remainder_map[t%60] = 1 + remainder_map.get(t%60,0)
        return count