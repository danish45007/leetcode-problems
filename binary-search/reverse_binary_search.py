def binary_search_on_reversed_array(arr,target):
    start = 0
    end = len(arr)
   
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif(arr[mid] < target):
            end = mid + 1
        elif(arr[mid] > target):
            start = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3,2]
    t = 4
    print(binary_search_on_reversed_array(arr,t))
      