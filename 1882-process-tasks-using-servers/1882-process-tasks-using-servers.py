class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available_heap = [] #[weight,index]
        unavailable_heap = [] #[free_time,weight,index]
        for idx,wt in enumerate(servers):
            heapq.heappush(available_heap,(wt,idx))
        
        time = 0
        res = [0]*len(tasks)
        for i,task_time in enumerate(tasks):
            time = max(i,time)
            # if the available_heap is empty
            if len(available_heap) == 0:
                time = unavailable_heap[0][0]
            while unavailable_heap and unavailable_heap[0][0] <= time:
                # can push the unavailable task into available_heap
                free_time,wt,idx = heapq.heappop(unavailable_heap)
                # push back the into available heap
                heapq.heappush(available_heap,(wt,idx))
            
            # get the avail server and assign the task to it
            wt,idx = heapq.heappop(available_heap)
            res[i] = idx
            # once task is assigned it will become unavailable
            heapq.heappush(unavailable_heap,(task_time+time,wt,idx))
        return res
                    