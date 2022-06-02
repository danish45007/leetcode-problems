class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # brute force solution O(n*8)
        N = len(cells)
        memo = {}
        while n:
            if str(cells) in memo:
                n %= memo[str(cells)] - n
            memo[str(cells)] = n
            if n > 0:
                temp_cells = [0]*N
                for i in range(1,7):
                    if cells[i-1] == cells[i+1]:
                        temp_cells[i] = 1
                    else:
                        temp_cells[i] = 0
                # done for 1 days
                # new cell state will be the state of prev day cell 
                cells = temp_cells
                n -=1
        return cells
        
        
                