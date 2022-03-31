def search_bitonic_array(arr,target):
    def get_pivot(arr):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end-start) // 2
            if(mid > 0 and mid < len(arr)-1):
                if(arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]):
                    return mid
                elif(arr[mid+1] > arr[mid]):
                    start = mid + 1
                elif(arr[mid-1]> arr[mid]):
                    end = mid - 1
            elif(mid == 0):
                if(arr[0] > arr[1]):
                    return 0
                else:
                    return 1
            elif(mid == len(arr) - 1):
                if(arr[len(arr)-1] > arr[len(arr)-2]):
                    return len(arr)-1
                else:
                    return len(arr)-2
    def search_in_inc_array(arr,start,end,target):
        while start <= end:
            mid = start + (end-start) // 2
            if(arr[mid] == target):
                return mid
            elif(target > arr[mid]):
                start = mid + 1
            elif(target < arr[mid]):
                end = mid - 1
        return -1
    def search_in_dec_array(arr,start,end,target):
        while start <= end:
            mid = start + (end-start) // 2
            if(arr[mid] == target):
                return mid
            elif(target > arr[mid]):
                end = mid - 1
            elif(target < arr[mid]):
                start = mid + 1
        return -1
    pivot = get_pivot(arr)
    if(pivot > target):
        return search_in_dec_array(arr,pivot+1,len(arr)-1,target)
    else:
        return search_in_inc_array(arr,0,pivot,target)

if __name__  == "__main__":
    print(search_bitonic_array([1,4,6,8,10,3,2],0))