class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0] # edges of flower can be consider as epmty spot
        for i in range(1,len(flowers)-1):
            # check if 3 contiguous is present to plant a flower
            if flowers[i-1] == 0 and flowers[i] == 0 and flowers[i+1] == 0:
                # plant flower
                flowers[i] = 1
                n -= 1
        return n <= 0