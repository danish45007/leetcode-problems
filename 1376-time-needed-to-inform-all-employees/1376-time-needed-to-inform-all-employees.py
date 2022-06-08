class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        time_to_inform = 0
        if n <= 0:  return 1
        manager_subordinate_map = defaultdict(list) #{manager:[subordinates]}
        visited = set()
        for idx,manager in enumerate(managers):
            manager_subordinate_map[manager].append(idx)
        
        def dfs(manager,time):
            nonlocal time_to_inform
            if manager in visited:
                return True
            visited.add(manager)
            time_to_inform =  max(time,time_to_inform)
            for sub in manager_subordinate_map[manager]:
                dfs(sub,time+informTime[sub])
                    
        
        dfs(headID,informTime[headID])
        return time_to_inform
            