class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1
        while right > left:
            mid = (left+right) // 2
            if arr[mid+1] > arr[mid]:
                left = mid + 1
            
            elif arr[mid+1] < arr[mid]:
                right = mid
                
        
        return left
                
        