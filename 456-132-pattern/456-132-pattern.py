class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [left_min,num]
        curr_min = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][1]:
                stack.pop()
            if stack and stack[-1][0] < n:
                return True
            stack.append([curr_min,n])
            curr_min = min(curr_min,n)
        print(stack)
        return False