class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
    
        l, r = 0, len(arr) - 1
        
        while l < (len(arr) - 1) and arr[l + 1] > arr[l]:
            l += 1
        
        while r > 1 and arr[r - 1] > arr[r]:
            r -= 1
            
        return (l == r) and l+1 != len(arr)