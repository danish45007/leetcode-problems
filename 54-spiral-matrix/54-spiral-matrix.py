class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        while left < right and top < bottom:
            # getting all elements from left to right in the top row
            for i in range(left,right):
                result.append(matrix[top][i])
            # move top down by 1
            top += 1
            # getting all elements from top to bottom in the right most column
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            # move the right towards left by 1
            right -=1
            # for single row or single column matrix
            if left >= right or top >= bottom:
                break
            # getting all elements from right to left for bottom most row
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom -=1
            # getting all the elements from bottom to top for left most column
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            # inc the left 
            left +=1
        return result