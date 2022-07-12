class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sq_num(n)
            if n == 1:
                return True
        return False
    
    def sq_num(self,n):
        output = 0
        while n:
            dig = n%10
            square = dig**2
            output += square
            n = n//10
        return output
            
        