class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # edge case
        if(len(nums) == 1):
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end-start) // 2
            mid_val,left_of_mid,right_of_mid = nums[mid],nums[mid-1] if mid > 0 else float('-inf'),nums[mid+1] if mid < len(nums)-1 else float('-inf')
            # found peak
            if left_of_mid < mid_val > right_of_mid:
                return mid
            elif left_of_mid < mid_val < right_of_mid:
                start = mid + 1
            else:
                end = mid - 1
                
                