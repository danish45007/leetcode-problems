class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lookup = {piece[0]: piece for piece in pieces}
        res = []
        for num in arr:
            if num in lookup:
                res.extend(lookup[num])
        return arr == res