class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col = len(mat),len(mat[0])
        curr_row = curr_col = 0
        res = []
        going_up = True
        while len(res) != row*col:
            
            if going_up:
                # incase of going up row is getting decremented
                while curr_row >= 0 and curr_col < col:
                    res.append(mat[curr_row][curr_col])
                    # move up and right
                    curr_row -=1
                    curr_col +=1
                
                # curr_row and curr_col out of bound
                
                # in case along the longest diagonal
                if curr_col == col:
                    curr_col -=1
                    curr_row +=2
                else:
                    curr_row +=1
                going_up = False
            else:
                # incase of going down col is getting decremented
                while curr_col >= 0 and curr_row < row:
                    res.append(mat[curr_row][curr_col])
                    # move down and left
                    curr_row +=1
                    curr_col -=1
                
                # curr_row and curr_col out of bound
                
                # in case along the longest diagonal
                # row out of bound
                if curr_row == row:
                    curr_col +=2
                    curr_row -=1
                else:
                    curr_col +=1
                going_up = True
        return res
                    
        