def almost_sorted_array_bs(nums,target):
    start = 0
    end = len(nums) -1
    while start <= end:
        mid = start + (end-start) // 2
        if(nums[mid] == target):
            return mid
        if(mid-1 >= start and nums[mid-1] == target):
            return mid - 1
        if(mid+1 <= end and nums[mid+1] == target):
            return mid + 1
        if(nums[mid] >= target): 
            end = mid - 2
        if(nums[mid] <= target):
            start = mid + 2
    return -1

print(almost_sorted_array_bs([5,10,30,20,40],10))
            