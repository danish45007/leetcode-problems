class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        # check all possible 2 cities combinations
        res = 0
        for city1 in range(n):
            for city2 in range(city1+1,n):
                common_road = 1 if city1 in graph[city2] else 0
                city1_connections = len(graph[city1])
                city2_connections = len(graph[city2])
                tota_connections = city1_connections + city2_connections - common_road
                res = max(res,tota_connections)
        return res