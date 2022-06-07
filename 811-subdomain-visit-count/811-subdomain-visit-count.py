class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = set()
        count_map = {}
        for domain in cpdomains:
            count,d = domain.split(' ')
            count = int(count)
            sub_domains = d.split('.')
            for i in range(len(sub_domains)):
                sub_domain = ".".join(sub_domains[i:])
                count_map[sub_domain] = count + count_map.get(sub_domain,0)
        
        for domain,count, in count_map.items():
            res.add(str(count) + ' ' + domain)
        return res

