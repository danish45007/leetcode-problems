### 解题思路

- - -
### 题解代码
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        for i in range(1,len(nums)):
            # swape required
            if((i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i -1 ])):
                nums[i],nums[i-1] = nums[i-1], nums[i]
        return nums

