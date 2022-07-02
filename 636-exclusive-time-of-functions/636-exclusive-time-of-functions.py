class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*(n)
        stack = [] #[[id,start_time,child_time]]
        for log in logs:
            log = log.split(':') #[id,'start/end','time']
            if log[1] == 'start':
                stack.append([log[0],log[2],0])
            else:
                # calculate the time consumed
                # poping out the start pair
                start_pair = stack.pop()
                time_interval = int(log[2]) - int(start_pair[1]) + 1
                # substracting the child time
                time_consumed = time_interval - int(start_pair[2])
                res[int(log[0])] += time_consumed
                if stack:
                    stack[-1][2] += time_interval
        return res
                    
                    