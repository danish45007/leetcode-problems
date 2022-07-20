class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        rank_to_idex_map = {}
        for idx,score in enumerate(scores):
            rank_to_idex_map[score] = idx
        res = [0]*len(scores)
        top_count = 1
        for score in sorted(scores,reverse=True):
            if top_count == 1:
                res[rank_to_idex_map[score]] = 'Gold Medal'
            elif top_count == 2:
                res[rank_to_idex_map[score]] = 'Silver Medal'
            elif top_count == 3:
                res[rank_to_idex_map[score]] = 'Bronze Medal'
            else:
                res[rank_to_idex_map[score]] = str(top_count)
            top_count +=1
        return res