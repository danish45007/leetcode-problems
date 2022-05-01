class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using Floyd's Cycle Detection
        """
            Time: O(n)
            Space: O(1)
        """
        # as the per the question there are exactly n+1 elements for nums in range [1,n] so according topigeon hole principle
        # these is exactly one duplicate element
        
        # step 1
        # find the frist intersection point where slow and fast pointer meets this will give the start of the cycle
        slow,fast = 0,0
        while True:
            # move single step
            slow = nums[slow]
            # move 2 steps
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # step 2
        # using the slow pointer and initializing a new pointer from 0 point of intersection will be the duplicate number
        duplicate = 0
        while True:
            slow = nums[slow]
            duplicate = nums[duplicate]
            if slow == duplicate:
                return duplicate
        
