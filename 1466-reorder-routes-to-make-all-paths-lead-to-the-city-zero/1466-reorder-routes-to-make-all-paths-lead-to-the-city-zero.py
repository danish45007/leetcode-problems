class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        changes = 0
        # set of current edges
        current_edges = {(a,b) for a,b in connections} #(city,neighbour)
        # construct a city to neighbour adjacency list
        city_neighbour = {i:[] for i in range(n)}
        # populate valid_edges data into the adjacency list
        for a,b in current_edges:
            city_neighbour[a].append(b)
            city_neighbour[b].append(a)
        # dfs to traverse
        def dfs(city):
            nonlocal visited, changes
            for neighbour in city_neighbour[city]:
                if neighbour in visited:
                    continue
                # not a valid edge
                if (neighbour,city) not in current_edges:
                    changes +=1
                visited.add(neighbour)
                dfs(neighbour)
        visited.add(0)
        dfs(0)
        return changes
                
                    
                

                 
        