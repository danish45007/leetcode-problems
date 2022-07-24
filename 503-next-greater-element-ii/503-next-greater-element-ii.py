class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return res