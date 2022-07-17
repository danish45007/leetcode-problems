class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_size = len(isConnected)
        visited = set()
        adjacent_cities = {i:[] for i in range(city_size)}
        for city in range(city_size):
            for connected_cities_idx in range(city_size):
                if isConnected[city][connected_cities_idx] == 1:
                    adjacent_cities[city].append(connected_cities_idx)
        def dfs(city):
            visited.add(city)
            for neighbour in adjacent_cities[city]:
                if neighbour not in visited:
                    dfs(neighbour)
                
        
        res = 0
        for city in range(city_size):
            if city not in visited:
                dfs(city)
                res +=1
        return res
                