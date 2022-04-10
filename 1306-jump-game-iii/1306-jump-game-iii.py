class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        cache = set()
        queue = deque()
        queue.append(start)
        cache.add(start)
        while queue:
            index = queue.popleft()
            # target condition
            if arr[index] == 0:
                return True
            # 2 possibilities (index-arr[index],index+arr[index])
            for x in ((index-arr[index]),index+arr[index]):
                # break condition
                if(0<=x<len(arr) and x not in cache):
                    queue.append(x)
                    cache.add(x)
        return False