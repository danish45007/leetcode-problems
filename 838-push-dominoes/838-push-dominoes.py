class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        queue = deque()
        for index,dom in enumerate(dominoes):
            if dom != '.':
                queue.append((index,dom))
        
        while queue:
            index,dom = queue.popleft()
            # in case of left falling
            if dom == "L":
                if index-1 >= 0 and dominoes[index-1] == ".":
                    queue.append((index-1,"L"))
                    dominoes[index-1] = "L"
            elif dom == "R":
                if(index+1 < len(dominoes) and index+2 < len(dominoes) and dominoes[index+1] == '.' and dominoes[index+2] == "L"):
                    queue.popleft()
                elif index+1 < len(dominoes) and dominoes[index+1] == ".":
                    queue.append((index+1,"R"))
                    dominoes[index+1] = "R"
        return "".join(dominoes)
                    
                    
                    
            