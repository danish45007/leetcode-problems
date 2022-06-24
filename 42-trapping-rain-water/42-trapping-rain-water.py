class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0,len(height)-1
        left_max,right_max = height[l],height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                res += min(left_max,right_max)-height[l] if min(left_max,right_max)-height[l] > 0 else 0
                left_max = max(left_max,height[l])
            else:
                r -=1
                res += min(left_max,right_max)-height[r] if min(left_max,right_max)-height[r] > 0 else 0
                right_max = max(right_max,height[r])
        return res