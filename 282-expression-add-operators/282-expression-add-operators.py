class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        '''
            i: current index
            prev: prev number
            curr: current number
            value: result of operation
            s: string expression
        '''
        def backtrack(i,prev,curr,value,s):
            if i == n:
                # curr == 0 to enusure no tailing number
                if value == target and curr == 0:
                    res.append(s)
                return
            curr = curr*10 + int(num[i])
            # case where we can concatenate curr number into prev number
            if curr > 0:
                backtrack(i+1,prev,curr,value,s)
            # when its the first char
            if not s:
                backtrack(i+1,curr,0,curr,str(curr))
            else:
                # all 3 possible case + , - , /
                # addition
                backtrack(i+1,curr,0,value+curr,s+'+'+str(curr))
                # substraction
                backtrack(i+1,-curr,0,value-curr,s+'-'+str(curr))
                # multiple
                backtrack(i+1,prev*curr,0,(value-prev)+(prev*curr),s+'*'+str(curr))
            
        n = len(num)
        res = []
        backtrack(0,0,0,0,'')
        return res
            