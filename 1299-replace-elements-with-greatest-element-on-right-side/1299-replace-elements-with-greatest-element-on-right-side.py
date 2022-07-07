class Solution(object):
    def replaceElements(self, arr):
        right_max = -1
        for i in range(len(arr)-1,-1,-1):
            new_max_val = max(right_max,arr[i])
            arr[i] = right_max
            right_max = new_max_val
        return arr
            
            
        