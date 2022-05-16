class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        word_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                word_map[pattern].append(word)
        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    nei_words = word_map[pattern]
                    for w in nei_words:
                        if w not in visited:
                            visited.add(w)
                            queue.append(w)
            res +=1
        return 0