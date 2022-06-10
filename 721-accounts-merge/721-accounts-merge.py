class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)                
                email_to_name[email] = name
        visited =set()
        stack = []
        result = []
        for email in graph:
            if email not in visited:
                stack.append(email)
                visited.add(email)
                
            res_local = []
            while stack:
                node = stack.pop()
                res_local.append(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)
            if res_local:    
                result.append([email_to_name[email]] + sorted(res_local))
        return result
            
            
                