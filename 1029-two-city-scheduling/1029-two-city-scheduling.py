class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        price_diff = []
        min_cost = 0
        for cost in costs:
            diff = cost[1] - cost[0]
            price_diff.append([diff,cost[0],cost[1]])
        price_diff.sort()
        for i in range(len(price_diff)):
            if(i < len(price_diff) // 2):
                min_cost += price_diff[i][2]
            else:
                min_cost += price_diff[i][1]
        return min_cost
        