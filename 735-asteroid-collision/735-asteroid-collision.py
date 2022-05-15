class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # collision happen
            while stack and stack[-1] > 0 and asteroid < 0:
                collision = stack[-1] + asteroid
                if collision > 0:
                    asteroid  = 0
                elif collision < 0:
                    stack.pop()
                elif collision == 0:
                    stack.pop()
                    asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)
        return stack
                    
        