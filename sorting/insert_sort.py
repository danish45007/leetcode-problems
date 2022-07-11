def solve(nums):
    # assuming the first element in nums is sorted
    
    # check for all unsorted elements and comparing with the sorted list
    for i in range(1,len(nums)-1):
        unsorted_element = nums[i]
        sorted_index = i
        # check with sorted list
        while nums[sorted_index-1] > unsorted_element and sorted_index > 0:
            nums[sorted_index] = nums[sorted_index-1]
            sorted_index -=1
        nums[sorted_index] = unsorted_element
    return nums

if __name__ == "__main__":
    print(solve([5,3,2,1,4]))