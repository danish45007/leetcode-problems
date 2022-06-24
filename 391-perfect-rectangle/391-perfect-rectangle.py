class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner_point = set()

        for x,y,a,b in rectangles:
            area+=(a-x)*(b-y)
            for points in [(x,y),(x,b),(a,y),(a,b)]:
                if points in corner_point:
                    corner_point.remove(points)
                else:
                    corner_point.add(points)

        if len(corner_point)!=4: # a rectangle should only have 4 corner points
            return False
        # check the area is equal or not 
        corner_point = sorted(list(corner_point), key = lambda x:(x[0], x[1]))
        return area == ((corner_point[-1][0]-corner_point[0][0])*(corner_point[-1][1]-corner_point[0][1]))