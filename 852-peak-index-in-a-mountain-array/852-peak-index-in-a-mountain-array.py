class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if(mid > 0 and mid < (len(arr) - 1)):
                if(arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]):
                    return mid
                elif(arr[mid+1] > arr[mid]):
                    start = mid + 1
                elif(arr[mid-1] > arr[mid]):
                    end = mid - 1
            elif(mid == 0):
                if(arr[0] > arr[1]):
                    return 0
                else:
                    return 1
            elif(mid == len(arr)-1):
                if(arr[len(arr)-1] > arr[len(arr)-2]):
                    return len(arr)-1
                else:
                    return len(arr)-2