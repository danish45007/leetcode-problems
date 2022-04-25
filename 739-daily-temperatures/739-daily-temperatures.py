class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[[stack_index,stack_temp]]
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx,stack_temp = stack.pop()
                res[stack_idx] = (i-stack_idx)
            stack.append([i,temp])
        return res
                
                