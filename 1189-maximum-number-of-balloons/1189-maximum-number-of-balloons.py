class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        inputTestHashMap = Counter(text)
        balloonHashMap = Counter("balloon")
        res = float(inf)
        for c in balloonHashMap:
            res = min(res,inputTestHashMap[c]//balloonHashMap[c])
        return res
        