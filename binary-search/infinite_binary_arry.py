def search_infinite_binary_array(arr):
    start = 0
    end = 1
    # first 1 occurrence
    target = 1
    res = -1
    while target > arr[end]:
        start = end
        end = end * 2
    while start <= end:
        mid = start + (end-start)//2
        if(arr[mid] == target):
            res = mid
            end = mid - 1
        if(target > arr[mid]):
            start = mid +1
        if(target < arr[mid]):
            end = mid - 1
    return res

if __name__ == "__main__":
    print(search_infinite_binary_array(arr=[0,0,0,0,0,0,0,1,1,1,1,1,1,1]))