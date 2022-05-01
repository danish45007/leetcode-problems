class RandomizedSet:

    def __init__(self):
        self.stack = []

    def insert(self, val: int) -> bool:
        if val not in self.stack:
            self.stack.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.stack:
            self.stack.pop(self.stack.index(val))
            return True
        return False

    def getRandom(self) -> int:
        if(len(self.stack)):
            return random.choice(self.stack)
        return []


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()