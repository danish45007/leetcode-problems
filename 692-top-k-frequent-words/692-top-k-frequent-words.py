class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] = 1 + word_freq.get(word,0)
        
        max_heap = [] # (freq,word)
        for word,count in word_freq.items():
            heapq.heappush(max_heap,(-count,word))
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
        