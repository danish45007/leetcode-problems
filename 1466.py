def minReorder(n, connections):
         # start at city 0
        # recursively check its neighbors
        # count outgoing edges
        
        edges = {(a,b) for a,b in connections}
        neighbour = {city:[] for city in range(n)}
        
        visited = set()
        changed = 0
        for a,b in connections:
            neighbour[a].append(b)
            neighbour[b].append(a)
        print(neighbour[0])
        def dfs(city):
            nonlocal edges,changed,visited,neighbour
            for ne in neighbour[city]:
                if ne in visited:
                    continue
               # check if neighbour can reach city 0
                if (ne,city) not in edges:
                    changed +=1
                visited.add(ne)
                dfs(ne)
                
        visited.add(0)
        dfs(0)
        return changed


if __name__ == "__main__":
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(minReorder(n,connections=connections))