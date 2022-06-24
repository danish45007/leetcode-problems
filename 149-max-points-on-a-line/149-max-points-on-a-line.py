class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        # return (slope,intercept)
        def find_line(x0,x1,y0,y1):
            # in case horizontal line (y0 == y1)
            if y0 == y1:
                return (0,y0)
            
            # in case of vertical line (x0 == x1)
            if x0 == x1:
                return x0,None
            else:
                slope = (y1-y0) / (x1-x0)
                intercept = y0 - slope*x0
                return (slope,intercept)
        
        line_to_point_map = defaultdict(set) #{line:set of points}
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                point1,point2 = points[i],points[j]
                x0,y0 = point1
                x1,y1 = point2
                line = find_line(x0,x1,y0,y1)
                line_to_point_map[line].add(i)
                line_to_point_map[line].add(j)
        max_point = 0
        for line,pnts in line_to_point_map.items():
            max_point = max(max_point,len(pnts))
        return max_point
                
                
            