class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.result = set()
        self.max_size = float('-inf')
        self.dfs(s,0,[],0,0)
        return self.result
    def dfs(self,string,curr_index,curr_res,left_count,right_count):
        # base condition
        if curr_index >= len(string):
            # if valid parantheses
            if left_count == right_count:
                if len(curr_res) > self.max_size:
                    self.max_size = len(curr_res)
                    self.result = set()
                    self.result.add("".join(curr_res))
                elif len(curr_res) == self.max_size:
                    self.result.add("".join(curr_res))
        else:
            curr_char = string[curr_index]
            if curr_char == "(":
                # decesion 1. to add curr_char in into the curr_res
                curr_res.append('(')
                self.dfs(string,curr_index+1,curr_res,left_count+1,right_count)
                curr_res.pop()
                
                # decesion 2.. to include the curr_char into the curr_res
                self.dfs(string,curr_index+1,curr_res,left_count,right_count)
            elif curr_char == ')':
                self.dfs(string,curr_index+1,curr_res,left_count,right_count)
                if left_count > right_count:
                    curr_res.append(')')
                    self.dfs(string,curr_index+1,curr_res,left_count,right_count+1)
                    curr_res.pop()
            else:
                curr_res.append(curr_char)
                self.dfs(string,curr_index+1,curr_res,left_count,right_count)
                curr_res.pop()
                    
                    
                    
                    
                