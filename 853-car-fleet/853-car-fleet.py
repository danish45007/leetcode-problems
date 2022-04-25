class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # store the position.speed pair
        cars = [[p,s] for p,s in zip(position,speed)]
        # sort in reverse order
        cars.sort(reverse=True,key=lambda x:x[0])
        stack = []
        for pos,spe in cars:
            stack.append((target-pos)/spe)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            
