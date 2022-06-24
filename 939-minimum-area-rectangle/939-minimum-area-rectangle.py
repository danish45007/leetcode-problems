class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        visited_points = set()
        
        for x1,y1 in points:
            for x2,y2 in visited_points:
                # check in other point's exists to make rectangle valid
                if (x1,y2) in visited_points and (x2,y1) in visited_points:
                    # calcutate area
                    area = abs(x2-x1) * abs(y2-y1)
                    min_area = min(min_area,area)
            
            visited_points.add((x1,y1))
        return min_area if min_area != float('inf') else 0