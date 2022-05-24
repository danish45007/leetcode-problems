class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
            Time: O(n)
            Space: O(n)
        '''
#         nums_set = set([i for i in range(1,len(nums)+1)])
#         for num in nums:
#             if num in nums_set:
#                 nums_set.remove(num)
#         return nums_set
        
        # space optimization
        '''
            Time: O(n)
            Space: O(1)
        '''
        # marking the elements with -ve that are present
        for num in nums:
            num_index = abs(num) - 1
            nums[num_index] = -1 * abs(nums[num_index])
        res = []
        for i,num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res
        