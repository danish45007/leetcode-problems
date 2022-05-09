class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = set()
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for i,val in enumerate(trip):
                if val == target[i]:
                    match.add(i)
        
        return len(match) == 3