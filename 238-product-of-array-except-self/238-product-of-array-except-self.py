class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            solution[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            solution[i] *= post
            post *= nums[i]
            
        return solution
        