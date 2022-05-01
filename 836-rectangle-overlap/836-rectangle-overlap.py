class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # doesn't overlap is r2 is either on left,right,top,bottom non overlapping
        # r2 is in right of r1
        if(rec1[2] <= rec2[0]): return False
        # r2 is in left of r1
        if(rec1[0] >= rec2[2]): return False
        #r2 is top of r1
        if(rec2[1] >= rec1[3]): return False
        # r2 is bottom of r1
        if(rec1[1] >= rec2[3]): return False
        return True