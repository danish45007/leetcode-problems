class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        char_count_map = {}
        for char in s:
            char_count_map[char] = 1 + char_count_map.get(char,0)
        
        max_heap = [] #[count,char]
        for char,count in char_count_map.items():
            heapq.heappush(max_heap,[-count,char])
        prev = None
        while max_heap or prev:
            if not max_heap and prev:
                return ""
            count,char = heapq.heappop(max_heap)
            res += char
            count +=1
            if prev:
                heapq.heappush(max_heap,prev)
                prev = None
            if count != 0:
                prev = [count,char]
        return res
            
            