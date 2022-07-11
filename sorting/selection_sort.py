def solve(nums):
    for i in range(len(nums)):
        min_value = nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] < min_value:
                min_value = nums[j]
        
        min_value_index = nums.index(min_value,i)
        if nums[i] != nums[min_value_index]:
            nums[i],nums[min_value_index] = nums[min_value_index],nums[i]
    return nums


if __name__ == "__main__":
    print(solve([5,3,2,1,4]))