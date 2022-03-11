class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        response = []
        def back_track(open_count,close_count):
            if open_count == close_count == n:
                response.append("".join(stack))
            
            if open_count < n:
                stack.append("(")
                back_track(open_count+1,close_count)
                stack.pop()
            if open_count > close_count:
                stack.append(")")
                back_track(open_count,close_count+1)
                stack.pop()
        
        back_track(0,0)
        return response
                
                
                
        