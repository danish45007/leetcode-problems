class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        '''
            Time: O(n)
            Space: O(n)
        '''
        # _map = {}
        # for num in nums:
        #     _map[num] = 1 + _map.get(num,0)
        # for n,count in _map.items():
        #     if count > len(nums) // 2:
        #         return n
        
        '''
            Time: O(nlogn)
            Space: O(1)
        '''
#         nums.sort()
#         prev = nums[0]
#         if len(nums) == 1:
#             return prev
#         res = 1
#         for i in range(1,len(nums)):
#             if nums[i] == prev:
#                 res += 1
#             else:
#                 prev = nums[i]
#                 res = 1
            
#             if res > len(nums) // 2:
#                 return nums[i]
        
        '''
            Time: O(n)
            Space: O(1)
        '''
        res,count = 0,0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res