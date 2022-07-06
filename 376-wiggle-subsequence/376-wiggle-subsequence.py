class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 0
        '''
        -1 : down
        0  : same
        1  : up
        '''
        direction = 0
        if len(nums) < 2:
            return len(nums)
        for i in range(1,len(nums)):
            # moving up
            if nums[i] > nums[i-1]:
                # need to find the maximum along the path
                if direction == -1:
                    count +=1
                direction = 1
            elif nums[i] < nums[i-1]:
                if direction == 1:
                    count +=1
                direction = -1
        if direction == 0:
            count +=1
        else:
            count +=2
        return count