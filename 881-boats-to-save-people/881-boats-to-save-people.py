class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        boats = 0
        while l <= r:
            boats +=1
            remaining_weight = limit - people[r]
            if(r >= l and people[l] <= remaining_weight):
                l += 1
            r -=1
        return boats