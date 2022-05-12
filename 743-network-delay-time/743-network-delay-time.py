class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1,n+1)}
        
        for u,v,w in times:
            adjList[u].append((v,w))
            
        time = 0
        minHeap = [(0,k)]
        visit = set()
        
        while minHeap and len(visit) < n:
            w1,n1 = heapq.heappop(minHeap)
            
            visit.add(n1)
            time = max(time, w1)
            
            for n2, w2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2,n2))
                    
        return time if len(visit) == n else -1
    