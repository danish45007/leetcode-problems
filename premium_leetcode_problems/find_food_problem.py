'''

Description
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.



Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.


'''


from collections import deque



def solve(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    queue = deque() #((r,c,steps))
    visited = set()
    directions = [(0,1),(0,-1),(-1,0),(1,0)]
    
    # step 1 find the starting position '*'
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == '*':
                queue.append((r,c,0))
                visited.add((r,c))
                break
    
    # apply bfs to find the shorts distance
    while queue:
        for _ in range(len(queue)):
            curr_row,curr_col,steps = queue.popleft()
            # check if reached the target '#
            if matrix[curr_row][curr_col] == '#':
                return steps
            else:
                for inc_row,inc_col in directions:
                    new_row,new_col = curr_row + inc_row, curr_col + inc_col
                    # check for the boundary
                    if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS and matrix[new_row][new_col] != 'X':
                        if (new_row,new_col) not in visited:
                            queue.append((new_row,new_col,steps+1))
                            visited.add((new_row,new_col))
    return -1            
    






if __name__ == '__main__':
    print(solve([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))

