def min_diff_search(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start)//2
        if(arr[mid] == target):
            return arr[mid]
        if(target >= arr[mid]):
            start = mid + 1
        if(target <= arr[mid]):
            end = mid - 1
    left_nearest = end
    right_nearest = start
    if(abs(target-left_nearest) > abs(target-right_nearest)):
        return arr[right_nearest]
    else:
        return arr[left_nearest]

if __name__ == "__main__":
    print(min_diff_search([1,2,3,4,5,8,9],7))