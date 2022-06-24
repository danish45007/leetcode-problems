class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candy = set()
        for candy in candyType:
            unique_candy.add(candy)
        return min(len(candyType)//2,len(unique_candy))