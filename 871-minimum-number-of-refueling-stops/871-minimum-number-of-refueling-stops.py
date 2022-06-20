class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel_in_tank = startFuel
        heap = []
        stations.append([target,float('inf')])
        refuel = 0
        prev_dist = 0
        for station in stations:
            dist,cap = station
            dist_travelled = dist-prev_dist
            # fuel used to reach dist
            fuel_in_tank -= dist_travelled
            
            while heap and fuel_in_tank < 0:
                fuel_in_tank += -heapq.heappop(heap)
                refuel +=1
            if fuel_in_tank < 0:
                return -1
            heapq.heappush(heap,-cap)
            prev_dist = dist
        return refuel
        