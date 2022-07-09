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
        visited = set()
        while queue:
            word = queue.popleft()
            if word in visited:
                continue
            else:
                if word == '':
                    return True
                visited.add(word)
                for start_word in wordDict:
                    if word.startswith(start_word):
                        queue.append(word[len(start_word):])
        return False
                    
                    