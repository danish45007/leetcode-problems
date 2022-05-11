class Solution:
    def racecar(self, target: int) -> int:
        #(moves,pos,speed)
        queue = deque()
        visited = set()
        # start with speed 1
        queue.append((0,0,1))
        while queue:
            move,pos,speed = queue.popleft()
            if pos == target:
                return move
            if (pos,speed) in visited:
                continue
            else:
                visited.add((pos,speed))
                # fire 'A' cmnd
                queue.append((move+1,pos+speed,speed*2))
                # case where 'R' needs to get fired
                if ((speed > 0 and pos+speed > target) or (speed < 0 and pos+speed < target)):
                    speed = -1 if speed > 0 else 1
                    queue.append((move+1,pos,speed))
                    
            
            
            