class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = {i:[] for i in range(N)} # i: [cost,node]
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                man_dist = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append([man_dist,j])
                adj_list[j].append([man_dist,i])
                
        visited = set()
        heap = [[0,0]] # node,score
        res = 0
        # prim's algo
        while len(visited) < N:
            cost,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for neighbour_cost,neighbour_node in adj_list[node]:
                if neighbour_node not in visited:
                    heapq.heappush(heap,[neighbour_cost,neighbour_node])
        return res
                
        