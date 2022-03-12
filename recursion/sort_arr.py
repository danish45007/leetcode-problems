class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort_recursive(nums)
    def sort_recursive(self,nums):
        # base condition
        if len(nums) == 1:
            return nums
        # hypothesis
        tail_element = nums[len(nums)-1]
        nums.pop()
        self.sort_recursive(nums) 
        # induction
        return self.insert_recursive(nums,tail_element)
    
    def insert_recursive(self,nums,temp):
        # base condition
        if len(nums) == 0 or nums[len(nums)-1] <= temp:
            nums.append(temp)
            return nums
        # hypothesis
        tail_element = nums[len(nums)-1]
        nums.pop()
        self.insert_recursive(nums,temp)
        # induction
        nums.append(tail_element)
        return nums