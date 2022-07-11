def merge_sort(nums):
    # dividing the nums into smaller array
    if len(nums)>1:
        mid = len(nums)//2
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        merge_sort(left_nums)
        merge_sort(right_nums)
        i,j,k  = 0,0,0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i +=1
            else:
                nums[k] = nums[j]
                j +=1
            k+=1
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i +=1
            k+=1
        while j < len(right_nums):
            nums[k] = right_nums[j]
            j +=1
            k+=1
    return nums


if __name__ == "__main__":
    print(merge_sort([4,1,6,2,7]))