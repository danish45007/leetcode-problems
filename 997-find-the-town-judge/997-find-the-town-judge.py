class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_list = defaultdict(int) #{person:trust}
        trusted_list = defaultdict(int)
        for person,trust_person in trust:
            trust_list[person] += 1 
            trusted_list[trust_person] +=1
        for person in range(1,n+1):
            # judge
            if trust_list[person] == 0 and trusted_list[person] == n-1:
                return person
        return -1