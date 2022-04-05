class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if(len(A) > len(B)):
            A,B = B,A
            
        start = 0
        end = len(A) - 1
        total_len = len(A) + len(B)
        total_half = total_len // 2
        while True:
            i = (start + end) // 2
            j = total_half - i - 2
            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if (i+1) < len(A) else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j+1] if (j+1) < len(B) else float('inf')
            
            # check for the valid partion
            if(A_left <= B_right and B_left <= A_right):
                # if odd
                if(total_len % 2):
                    return min(A_right,B_right)
                else:
                    return (max(A_left,B_left)+min(A_right,B_right)) / 2
            elif(A_left > B_right):
                end = i - 1
            elif(B_left > A_right):
                start = i + 1
                