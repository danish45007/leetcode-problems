class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for i in range(1,len(arr)-1):
            # find the peak element except[0th and last element]
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                start=end = i
                while start > 0 and arr[start] > arr[start-1]:
                    start -=1
                while end+1 < len(arr) and arr[end] > arr[end+1]:
                    end +=1
                res = max(res,end-start+1)
        return res
            
            