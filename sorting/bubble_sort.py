def bubble_sort(nums):
    _sorted = False
    while not _sorted:
        _sorted = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                _sorted = False
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums

print(bubble_sort([4,3,2,1]))