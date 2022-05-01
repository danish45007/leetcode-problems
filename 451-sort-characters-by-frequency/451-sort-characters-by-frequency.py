class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        char_freq_map = {}
        res = ''
        for char in s:
            char_freq_map[char] = 1 + char_freq_map.get(char,0)
        for key,val in char_freq_map.items():
            heapq.heappush(heap,(-val,key))
        while heap:
            key,val = heapq.heappop(heap)
            res += -key*val
        return res