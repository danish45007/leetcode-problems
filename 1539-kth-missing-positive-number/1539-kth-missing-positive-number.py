class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num_set = set()
        for num in arr:
            num_set.add(num)
        missing_count = 0
        for i in range(1,10001):
            if i not in num_set:
                missing_count +=1
            if missing_count == k:
                return i