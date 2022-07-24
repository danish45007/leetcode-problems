class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for num in nums:
            # check if new sequence will start:
            if not res or num != res[-1][-1]+1:
                res.append([num])
            else:
                res[-1].append(num)
        # format res
        for i,rng in enumerate(res):
            if len(rng) > 1:
                res[i] = f"{rng[0]}->{rng[-1]}"
            else:
                res[i] = f"{rng[0]}"
        return res
            