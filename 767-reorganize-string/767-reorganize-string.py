class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        char_count = {}
        for char in s:
            char_count[char] = 1 + char_count.get(char,0)
        
        max_heap = [] #[(char_count,char)]
        for char,count in char_count.items():
            heapq.heappush(max_heap,(-count,char))
        
        while len(max_heap) >= 2:
            top_most_count,top_most_char = heapq.heappop(max_heap)
            next_count,next_char = heapq.heappop(max_heap)
            
            res.append(top_most_char)
            res.append(next_char)
            
            if top_most_count + 1 != 0:
                heapq.heappush(max_heap,(top_most_count+1,top_most_char))
            
            if next_count + 1 != 0:
                heapq.heappush(max_heap,(next_count+1,next_char))
        
        # only one odd char left to get processed
        if max_heap:
            char_count,char = heapq.heappop(max_heap)
            # not a valid case to add into result
            if -char_count > 1 or res[-1] == char:
                return ''
            res.append(char)
        return ''.join(res)
            
            
            
            