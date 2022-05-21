class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        # generate total number of valid Interchangeable rectangle count
        for w,h in rectangles:
            count[w/h] = 1 + count.get(w/h,0)
        # for each count find the total pair of combinations
        # nC2 ~ n(n-1)/2
        res = 0
        for c in count.values():
            res += c*(c-1)//2
        return res
            