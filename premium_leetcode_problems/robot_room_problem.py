'''

Description
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
Example
Example 1:

Input：
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3
Explanation：
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Example 2:

Input：
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [1,0,0,1,0,0,0,1],
  [1,1,1,1,1,1,1,1]
],
row = 2,
col = 3
Explanation：
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=2, col=3.
From the top left corner, its position is two rows below and three columns right.

'''


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        #write your code here
        # moving in all directions in clockwise
        '''
            0th index => going up
            1th index => going right
            2nd index => going down
            3rd index => going left
        '''
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        def go_back_to_prev():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x,y,curr_direction):
            visited.add((x,y))
            robot.clean()
            for i in range(4):
                new_direction = (curr_direction + i) % 4
                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]
                if (new_x,new_y) not in visited and robot.move():
                    dfs(new_x,new_y,new_direction)
                    go_back_to_prev()
                
                robot.turnRight()
        dfs(0,0,0)

