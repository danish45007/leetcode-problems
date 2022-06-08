class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_count = {0:0}
        for row in wall:
            total_gap = 0
            # dont consider the right edge of row
            for brick in row[:-1]:
                total_gap += brick
                gap_count[total_gap]= 1 + gap_count.get(total_gap,0)
        
        return len(wall) - max(gap_count.values())