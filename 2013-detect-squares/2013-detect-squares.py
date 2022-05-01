class DetectSquares:

    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.points:
            # using the current point and query point check if the points can form valid square or not
            # width == height
            if(abs(x-px) != abs(y-py) or x == px or y == py):
                continue
            # check the count of the diagonals to generate the no .of squares
            res += self.point_count[(px,y)] * self.point_count[(x,py)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)