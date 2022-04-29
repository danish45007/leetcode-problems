class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n

        def dfs(start: int):
            seen[start] = True
            for other in range(n):
                if isConnected[start][other] and not seen[other]:
                    dfs(other)
        
        ans = 0
        for city in range(n):
            if not seen[city]:
                ans += 1
                dfs(city)
        return ans