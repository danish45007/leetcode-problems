class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # converting the dominoes<type:str> into <type:array> to able to mutate values at indices
        dominoes = list(dominoes)
        queue = deque() #[index,state(left/right)]
        # adding non standing dominoes (left/right) into queue
        # as these are responsible for changing the state of other dominoes
        for index,dom in enumerate(dominoes):
            if dom != '.':
                queue.append((index,dom))
        
        while queue:
            index,dom = queue.popleft()
            # in case of left falling
            if dom == "L":
                # checking the prev dominoe if standing then standing its state to left
                if index-1 >= 0 and dominoes[index-1] == ".":
                    # adding prev left falling dominoes into queue as it can be responsible for chaning the state of its prev dominoe
                    queue.append((index-1,"L"))
                    dominoes[index-1] = "L"
            # in case of left falling
            elif dom == "R":
                # case Right -> Standing <- Left
                # will have no impact on the state of 3 contiguous dominoe
                if(index+1 < len(dominoes) and index+2 < len(dominoes) and dominoes[index+1] == '.' and dominoes[index+2] == "L"):
                    # need to pop out the one falling toward left as its been proccessed
                    queue.popleft()
                # case Right -> Standing similar the left falling
                elif index+1 < len(dominoes) and dominoes[index+1] == ".":
                    queue.append((index+1,"R"))
                    dominoes[index+1] = "R"
        # cnverting back array into str type
        return "".join(dominoes)
                    
                    
                    
            