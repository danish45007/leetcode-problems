class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        min_boat = 0
        l,r = 0,len(people)-1
        while l <= r:
            remain_wt = limit-people[r]
            min_boat += 1
            r -= 1
                
            if(r >= l and people[l] <= remain_wt):
                l += 1
        
        return min_boat