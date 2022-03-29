def search_in_infinite_array(arr,target):
    start = 0
    end = 1
    while (target > arr[end]):
        start = end
        end = end*2
    while (start <= end):
        mid = start + (end - start) // 2
        if(arr[mid] == target):
            return mid
        if(target >= arr[mid]):
            start = mid + 1 
        if(target <= arr[mid]):
            end = mid - 1
    return -1      

if __name__ == "__main__":
    print(search_in_infinite_array(arr=[2, 5, 7, 9, 10, 12, 15, 16, 18, 20, 24, 28, 32, 35],target=16))