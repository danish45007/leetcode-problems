class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        0,0 -> 0,n-1
        0,1 -> 1,n-1
        0,2 -> 2,n-2
        n,n -> n,N-n
        """
        left,right = 0,len(matrix)-1
        while right > left:
            # no of rotatins (n-1)
            for i in range(right-left):
                top,bottom = left,right
                # anti-clock rotation
                tempTopLeft = matrix[top][left+i]
                # move bottom-left into top-left
                matrix[top][left+i] = matrix[bottom-i][left]
                # move bottom-right into buttom-left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # move top-right into bottom-right
                matrix[bottom][right-i] = matrix[top+i][right]
                # move the top=left temp var into top-right
                matrix[top+i][right] = tempTopLeft
            right -= 1
            left +=1
                
                
        
        