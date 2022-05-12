class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        src_dst_list = {src:[] for src,dst in tickets}
        for src,dst in tickets:
            src_dst_list[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in src_dst_list:
                return False
            temp = src_dst_list[src]
            for i,v in enumerate(temp):
                res.append(v)
                src_dst_list[src].pop(i)
                if dfs(v):
                    return True
                else:
                    # backtrack
                    res.pop()
                    src_dst_list[src].insert(i,v)
            return False
        dfs("JFK")
        return res
                    

        