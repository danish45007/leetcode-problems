class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        l,r = 0,len(height)-1
        l_max,r_max = height[l],height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                l +=1
                l_max = max(l_max,height[l])
                res += l_max - height[l]
            else:
                r -=1
                r_max = max(r_max,height[r])
                res += r_max - height[r]
        return res
        
        