class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def generate_all_possible_mutations(mutation):
            result = []
            possible_char = ['A','C','G','T']
            for i in range(len(mutation)):
                for char in possible_char:
                    result.append(mutation[0:i] + char + mutation[i+1:])
            return result
                        
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        bank = set(bank)
        min_mutations = 0
        while queue:
            for _ in range(len(queue)):
                mutation = queue.popleft()
                if mutation == end:
                    return min_mutations
                all_mutations = generate_all_possible_mutations(mutation)
                for gene in all_mutations:
                    if gene in bank and gene not in visited:
                        queue.append(gene)
                        visited.add(gene)
            min_mutations +=1
        return -1