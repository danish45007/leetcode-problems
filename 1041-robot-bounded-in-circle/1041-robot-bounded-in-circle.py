class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # current direction assuming its facing towards north
        dir_x,dir_y = 0,1
        # starting from the origin
        x,y = 0,0
        for d in instructions:
            if d == "G":
                # update the x,y by along direction
                x = x + dir_x
                y = y + dir_y
            elif d == "L":
                # rotate direction by -90
                dir_x,dir_y = -1*dir_y,dir_x
            else:
                dir_x,dir_y = dir_y,-1*dir_x
        # after following the instructions if the x,y ends up back to origin
        # or the direction by the end of iteration changed
        # implies it will fall into endless cycle
        return (x,y) == (0,0) or (dir_x,dir_y) != (0,1)