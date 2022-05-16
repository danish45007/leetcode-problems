class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        stack = [] #[(start_idx,height)]
        for index,height in enumerate(heights):
            # breaks the monotonic inc order
            new_index = index
            while stack and stack[-1][1] > height:
                # pop such heights to maintain the inc monotonic order
                start_idx,_height = stack.pop()
                width = index-start_idx
                area = _height * width
                max_area = max(max_area,area)
                new_index = start_idx
            stack.append([new_index,height])
        for i,h in stack:
            max_area = max(max_area,h*(len(heights)-i))
        return max_area
        
                       