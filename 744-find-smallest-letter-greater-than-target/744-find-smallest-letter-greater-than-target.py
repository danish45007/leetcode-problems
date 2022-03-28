class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # generalized into ceil of target char
        start = 0
        end = len(letters) - 1
        res = letters[0]
        while start <= end:
            mid = start + (end-start) // 2
            if(letters[mid] == target):
                start = mid + 1
            if(letters[mid] > target):
                res = letters[mid]
                end = mid - 1
            if(letters[mid] < target):
                start = mid + 1
        return res