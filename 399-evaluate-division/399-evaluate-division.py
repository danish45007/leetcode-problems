class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (x,y),value in zip(equations,values):
            graph[x].append((y,value))
            graph[y].append((x,1.0/value))
            
        def bfs(res,query):
            x,y = query
            queue = deque()
            queue.append((x,1.0)) # (node,inital_product)
            visited = set()
            visited.add(x)
            while queue:
                for _ in range(len(queue)):
                    node,product = queue.popleft()
                    if node not in graph:
                        res.append(-1.0)
                        return
                    if node == y:
                        res.append(product)
                        return
                    for neighbour,value in graph[node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append((neighbour,product*value))
            res.append(-1.0)
        res = []
        for query in queries:
            bfs(res,query)
        return res