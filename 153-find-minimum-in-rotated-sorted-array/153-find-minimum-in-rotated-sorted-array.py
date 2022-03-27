class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if(nums[l] <= nums[r]):
                return nums[l]
            mid = l + (r-l) // 2
            next_mid = (mid + 1) % len(nums)
            prev_mid = (mid + len(nums) - 1) % len(nums)
            if(nums[mid] <= nums[next_mid] and nums[mid] <= nums[prev_mid]):
                return nums[mid]
            # first half is already sorted 
            if(nums[l] <= nums[mid]):
                l = mid + 1
            # second half sorted
            if(nums[mid] <= nums[r]):
                r = mid - 1
        return -1
                