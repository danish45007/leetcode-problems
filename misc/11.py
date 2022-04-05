class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            height_ = min(height[left_pointer],height[right_pointer])
            area = width*height_
            max_area = max(area,max_area)
            
            if (height[left_pointer] > height[right_pointer]):
                right_pointer -= 1
            else:
                left_pointer += 1
            
        return max_area
