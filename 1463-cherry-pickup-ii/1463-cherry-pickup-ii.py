class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = {} #{(r,c1,c2): max_pick}
        # (r,c1) -> robot1 is starting from
        # (r,c2) -> robot2 is starting from
        def dfs(r,c1,c2):
            if (r,c1,c2) in dp:
                return dp[(r,c1,c2)]
            # giving priority to 1st robot to pick cherry
            curr_cherry = grid[r][c1]
            if c1 != c2:
                curr_cherry += grid[r][c2]
            
            if r == ROWS-1:
                return curr_cherry
            
            
            # moves for robot1
            robot_1_moves = [c1-1,c1,c1+1]
            # moves for robot2
            robot_2_moves = [c2-1,c2,c2+1]
            
            temp = 0
            for m1 in robot_1_moves:
                for m2 in robot_2_moves:
                    # work for only valid moves (r,c)
                    if m1 >= 0 and m2 >= 0 and m1 < COLS and m2 < COLS:
                        temp = max(temp,dfs(r+1,m1,m2))
            dp[(r,c1,c2)] = temp+curr_cherry
            return temp+curr_cherry
        return (dfs(0,0,COLS-1))