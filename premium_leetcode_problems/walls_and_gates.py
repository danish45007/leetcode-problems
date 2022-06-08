'''
Description
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF


Example
Example1

Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
Example2

Input:
[[0,-1],[2147483647,2147483647]]
Output:
[[0,-1],[1,2]]

'''

from typing import (
    List,
)

from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROW = len(rooms)
        COL = len(rooms[0])
        queue = deque()
        visited = set()
        # adding all the gates into queue

        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        def visit_dir(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL or (r,c) in visited or rooms[r][c] == -1:
                return
            queue.append((r,c))
            visited.add((r,c))

        # when starting from the gates the inital distance is 0
        distance = 0
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                r,c = queue.popleft()
                # marking (r,c) with curr distance
                rooms[r][c] = distance
                # visiting all 4 dirsctions
                visit_dir(r,c+1)
                visit_dir(r,c-1)
                visit_dir(r+1,c)
                visit_dir(r-1,c)
            # done processing a single layer
            distance +=1

