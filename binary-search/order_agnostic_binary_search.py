def order_agnostic_binary_search(arr,target):
    start = 0
    end = len(arr)
   
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif(arr[mid] < target and arr[0] > arr[len(arr)-1]):
            end = mid + 1
        elif(arr[mid] > target and arr[0] > arr[len(arr)-1]):
            start = mid - 1
        elif(arr[mid] < target and arr[0] < arr[len(arr)-1]):
            start = mid + 1
        elif(arr[mid] > target and arr[0] < arr[len(arr)-1]):
            end = mid - 1
	 
    return -1

if __name__ == "__main__":
    arr_desc = [9,8,7,6,5,4,3,2]
    arr_asce = [0,1,2,3,4,5,6,7,8]
    t = 4
    print(order_agnostic_binary_search(arr_asce,t))
      