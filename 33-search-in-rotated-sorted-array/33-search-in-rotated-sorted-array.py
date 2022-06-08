class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        def binary_search(start,end,nums,target):
            while start <= end:
                mid = start + (end-start) // 2
                if(nums[mid] == target):
                    return mid
                if(nums[mid] <= target):
                    start = mid + 1
                if(nums[mid] >= target):
                    end = mid - 1
            return -1
        def get_pivot(nums,start,end):
            while start <= end:
                # base case for sorted array
                if(nums[start] <= nums[end]):
                    return start
                mid = start + (end-start) // 2
                # smallest element 
                if(nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]):
                    return mid
                if(nums[start] <= nums[mid]):
                    start = mid + 1
                if(nums[end] >= nums[mid]):
                    end = mid - 1
            return -1
        pivot = get_pivot(nums,start,end)
        result_from_first_half = binary_search(start,pivot-1,nums,target)
        result_from_second_half = binary_search(pivot,end,nums,target)
        if(result_from_first_half > -1):
                return result_from_first_half
        elif(result_from_second_half > -1):
                return result_from_second_half
        else:
                return -1
                
        