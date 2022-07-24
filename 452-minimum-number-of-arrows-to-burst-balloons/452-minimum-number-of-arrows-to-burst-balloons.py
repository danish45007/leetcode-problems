class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prev_end = float('-inf')
        min_arrow = 0
        for start,end in points:
            # start with the prev_end
            if start <= prev_end:
                continue
            else:
                min_arrow +=1
                prev_end = end
        return min_arrow