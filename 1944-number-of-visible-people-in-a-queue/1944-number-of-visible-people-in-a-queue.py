class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0]*len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            height = heights[i]
            visible = 0
            while stack and stack[-1] < height:
                visible += 1
                stack.pop()
            if stack:
                visible +=1
            stack.append(height)
            res[i] = visible
        return res
                