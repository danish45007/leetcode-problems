class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topTarget = tops[0]
        buttomTarget = bottoms[0]
        
        for target in [topTarget,buttomTarget]:
            missingTop,missingButtom = 0,0
            for i, pair in enumerate(zip(tops,bottoms)):
                top,buttom = pair
                if not (top == target or buttom == target):
                    break
                if top != target:
                    missingTop +=1
                if buttom != target:
                    missingButtom +=1
                if i == len(tops) - 1:
                    return min(missingTop,missingButtom)
        
        return -1