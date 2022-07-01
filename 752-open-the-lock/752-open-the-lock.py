class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # base condition
        if "0000" in deadends:
            return -1
        # get all possible combination for each lock state
        def get_children(lock):
            res = []
            for i in range(4):
                # incase of incrementing value at each index
                res.append(lock[0:i] + str((int(lock[i])+1)%10) + lock[i+1:])
                # incase of decrementing value at each index
                res.append(lock[0:i] + str((int(lock[i])-1+10)%10) + lock[i+1:])
            return res
        # adding deadends into set as we have to avoid visting them
        visited = set()
        deadends = set(deadends)
        '''
            Apply dfs over the decision tree and at each level for the target to find the turns in shortest path
        '''
        queue = deque()
        # add the root lock state and init moves
        queue.append(["0000",0])
        
        while queue:
            # get the recent added lock state and move
            lock_state,move = queue.popleft()
            # check for the result
            if lock_state == target:
                return move
            for child_state in get_children(lock_state):
                # check if already visited or part of deadend
                if child_state not in visited and child_state not in deadends:
                    visited.add(child_state)
                    queue.append([child_state,move+1])
        return -1
            