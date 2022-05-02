class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        min_heap = []
        # reserve the index before sorting
        for i,task in enumerate(tasks):
            task.append(i)
        # sort the task based on the enqueue time
        tasks.sort(key=lambda x:x[0])
        i,time = 0,tasks[0][0]
        
        while i < len(tasks) or min_heap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap,[tasks[i][1],tasks[i][2]])
                i +=1
            
            if not min_heap:
                time = tasks[i][0]
            else:
                process_time,index = heapq.heappop(min_heap)
                time += process_time
                result.append(index)
        return result
                
                
