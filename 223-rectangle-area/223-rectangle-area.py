class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def get_area(x1,x2,y1,y2):
            height,breadth = y2-y1,x2-x1
            return height*breadth
        #area of rectange 1
        area_1 = get_area(ax1,ax2,ay1,ay2)
        #area of rectange 2
        area_2 = get_area(bx1,bx2,by1,by2)
        # overlapping dimensions
        x1,x2 = max(ax1,bx1),min(ax2,bx2)
        y1,y2 = max(ay1,by1),min(ay2,by2)
        area_overlap=0
        if x2 >= x1 and y2 >= y1:
            area_overlap = get_area(x1,x2,y1,y2)
        
        return area_1+area_2-area_overlap
        
        
        
        