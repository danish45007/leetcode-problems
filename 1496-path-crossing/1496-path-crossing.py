class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0,0)
        visited = set()
        visited.add(curr)
        for p in path:
            x,y = curr
            if p == 'N':
                curr = (x,y+1)
            elif p == 'S':
                curr = (x,y-1)
            elif p == 'E':
                curr = (x+1,y)
            else:
                curr = (x-1,y)
            if curr in visited:
                return True
            else:
                visited.add(curr)
        return False
            