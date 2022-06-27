class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # brute force using dfs
#         _map = {i:[] for i in range(n)}
#         for source,_dst,price in flights:
#             _map[source].append([_dst,price])
#         visited = set()
#         min_price = float('inf')
        
#         def dfs(node,k,price_so_far):
#             nonlocal visited,min_price
#             if node == None:
#                 return 0
#             visited.add(node)
#             for next_node,price in _map[node]:
#                 if(next_node == dst):
#                     min_price = min(price+price_so_far,min_price)
#                 else:
#                     if(next_node not in visited and k > 0):
#                         dfs(next_node,k-1,price_so_far+price)
#             visited.remove(node)
        
#         dfs(src,k,0)
#         return min_price if min_price != float('inf') else -1
            
        
        
        # Ballmen ford
        
        prices = [float("inf")]*n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices.copy()
            for s,d,p in flights:
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
        return prices[dst] if prices[dst] != float('inf') else -1
                