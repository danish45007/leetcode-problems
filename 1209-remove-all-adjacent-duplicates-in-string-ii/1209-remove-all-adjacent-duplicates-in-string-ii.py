class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = ""
        
        stack = [] #char,count
        for char in s:
            if not stack:
                stack.append([char,1])
            else:
                top,count = stack[-1]
                if top != char:
                    stack.append([char,1])
                else:
                    if count+1 == k:
                        stack.pop()
                    else:
                        stack[-1][1] +=1
        
        for char,count in stack:
            res += str(char*count)
        return res
                