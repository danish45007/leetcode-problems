class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task_freq = {}
        # # constructing a task frequency hashmap
        # for task in tasks:
        #     task_freq[task] = 1 + task_freq.get(task,0)
        # max_heap = []
        # # contructing a max heap
        # for key,val in task_freq.items():
        #     heapq.heappush(max_heap,-val)
        # time = 0
        # queue = deque()
        # while max_heap or queue:
        #     time +=1
        #     # pop out most freq task and process
        #     if max_heap:
        #         task_count = 1 + heapq.heappop(max_heap)
        #         # add the task_count into the queue for next time process
        #         if task_count < 0:
        #             queue.append([task_count,time+n])
        #     # check the top of the queue if falls under the given time then popout
        #     if(queue and queue[0][1] == time):
        #         # pop out the most recent one and push back into queue
        #         heapq.heappush(max_heap,queue.popleft()[0])
        # return time
        
        task_freq = {}
        for task in tasks:
            task_freq[task] = 1 + task_freq.get(task,0)
        
        max_heap = []
        for key,val in task_freq.items():
            heapq.heappush(max_heap,-val)
        time = 0
        queue = deque() #[task_count,time]
        while max_heap or queue:
            time += 1
            if max_heap:
                task_count = 1 + heapq.heappop(max_heap)
                
                if task_count < 0:
                    queue.append([task_count,time+n])
            
            if (queue and queue[0][1] == time):
                heapq.heappush(max_heap,queue.popleft()[0])
        return time
                
            