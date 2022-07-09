class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False]*(len(s)+1)
        # dp[len(s)] = True
        # for i in range(len(s)-1,-1,-1):
        #     for word in wordDict:
        #         if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
        #             dp[i] = dp[i+len(word)]
        #         if(dp[i]):
        #             break
        # return dp[0]
        queue = deque([s])
        def startswith_method(word,start_word):
            return word[:len(start_word)] == start_word
        visited = set()
        while queue:
            word = queue.popleft()
            if word in visited:
                continue
            else:
                if not word:
                    return True
                visited.add(word)
                for start_word in wordDict:
                    if startswith_method(word,start_word):
                        queue.append(word[len(start_word):])
        return False
                    
                    