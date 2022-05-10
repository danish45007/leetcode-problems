class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_route_map = defaultdict(list)
        for count,route in enumerate(routes):
            for bus in route:
                bus_route_map[bus].append(count)
        visited_buses_routes = set()
        visited_buses = set()
        moves = 0
        queue = deque()
        queue.append(source)
        visited_buses.add(source)
        while queue:
            for i in range(len(queue)):
                last_bus = queue.popleft()
                if last_bus == target:
                    return moves
                for route in bus_route_map[last_bus]:
                    if route in visited_buses_routes: continue
                    visited_buses_routes.add(route)
                    buses_in_route = routes[route]
                    for bus in buses_in_route:
                        if bus in visited_buses: continue
                        queue.append(bus)
                        visited_buses.add(bus)
            moves +=1
        return -1