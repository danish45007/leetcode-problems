class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side_length = sum(matchsticks)//4
        sides = [0]*len(matchsticks)
        # if side is not integer
        if sum(matchsticks)/4 != side_length:
            return False
        # to optimize the solution by checking if the larger matchstcik exceeds the side_length return False
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= side_length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    # backtrack for other input
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)
        