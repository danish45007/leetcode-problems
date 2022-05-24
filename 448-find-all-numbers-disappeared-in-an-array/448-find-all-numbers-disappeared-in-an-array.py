class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set([i for i in range(1,len(nums)+1)])
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
        return nums_set